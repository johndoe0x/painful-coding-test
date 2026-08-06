# NeetCode 500 Dashboard

한국어 우선, 로컬 전용 NeetCode 500 학습 대시보드입니다. 현재 브랜치는 **Foundation slice**만 구현합니다. 고정된 1년 계획, 서울 기준 달력, SQLite/Alembic, append-only 이벤트, 검증형 백업, 읽기 전용 Foundation UI가 준비되어 있습니다.

문제 500개 일정, 코드 실행·채점, 첫 3회 AI 코치, 6회 블라인드 반복, 음성 설명, 단계형 애니메이션은 아직 활성화하지 않습니다. 화면과 health API는 이를 `FOUNDATION_ONLY`로 명시합니다.

## 요구 사항

- Python 3.12 이상 (`.python-version`은 3.13)
- [uv](https://docs.astral.sh/uv/)
- macOS 또는 SQLite WAL을 지원하는 로컬 환경

## 소스 checkout 설치 및 실행

```bash
uv sync
uv run alembic upgrade head
uv run neetcode-dashboard --host 127.0.0.1 --port 8000
```

브라우저에서 `http://127.0.0.1:8000/`을 열고, 상태는 다음으로 확인합니다.

```bash
curl -fsS http://127.0.0.1:8000/api/health
```

지원하는 `neetcode-dashboard` CLI는 `127.0.0.1` 또는 `localhost`에만 바인딩하며, `0.0.0.0`과 외부 주소는 설정 검증 단계에서 거부합니다. 직접 Uvicorn으로 ASGI 앱을 공개 주소에 바인딩하는 방식은 지원하지 않으며, 실수로 그렇게 실행해도 애플리케이션 미들웨어가 비루프백 클라이언트 요청을 거부합니다.

## 데이터 위치

소스 checkout에서는 기본 실행 위치가 저장소 루트이고, 설치된 wheel에서는 실행한 현재 디렉터리가 기본 런타임 루트입니다. 공휴일 원본, 마스터 플랜, Alembic 설정과 migration은 wheel 안에도 함께 번들됩니다.

| 항목 | 기본 경로 |
|---|---|
| 학습 DB | `data/tracker.sqlite3` |
| 검증 백업 | `backups/` |
| 고정 공휴일 원본 | `data/holidays.json` |
| 고정 마스터 플랜 | `PLAN.md` |

테스트나 격리 실행에서는 `NEETCODE_PROJECT_ROOT`로 **런타임 DB와 백업 위치만** 옮길 수 있습니다. 공휴일 원본과 `PLAN.md` 계약은 소스 checkout 또는 설치된 wheel의 불변 리소스에 고정됩니다. 앱의 programmatic migration과 소스 checkout에서 실행하는 Alembic CLI 모두 같은 환경변수를 따릅니다.

```bash
NEETCODE_PROJECT_ROOT=/private/tmp/neetcode-foundation \
  uv run neetcode-dashboard --host 127.0.0.1 --port 8000
```

이 경우 DB는 `/private/tmp/neetcode-foundation/data/tracker.sqlite3`, 백업은 `/private/tmp/neetcode-foundation/backups/`에 생성됩니다.

설치된 wheel은 `neetcode-dashboard` 시작 시 번들된 설정과 migration으로 DB를 자동 업그레이드합니다. 빈 디렉터리의 일반 `alembic` 실행 파일은 설정 파일을 자동 발견하지 못하므로, 위 `uv run alembic ...` 명령과 아래 `alembic check`는 소스 checkout 전용입니다.

## 백업과 복원

앱이 실행 중이어도 SQLite backup API를 사용해 일관된 백업을 만들 수 있습니다.

```bash
uv run python -c 'from neetcode_dashboard.backup import create_verified_backup; from neetcode_dashboard.config import Settings; s=Settings(); print(create_verified_backup(s.database_path, s.backup_dir))'
```

각 백업은 `.sqlite3`와 `.manifest.json` 한 쌍입니다. manifest에는 앱 버전, Alembic revision, 생성 시각, `PLAN.md` SHA-256, DB SHA-256, 무결성 결과, 이벤트·공휴일 행 수가 기록됩니다. 발행과 복원 전에 모든 이벤트 스트림의 순서, canonical payload, payload hash, 이전/event hash, UTC 시각, 서울 기준 학습일을 다시 검증합니다.

복원할 때는 반드시 앱을 먼저 종료합니다. 아래의 두 경로를 실제 백업 파일명으로 바꿉니다.

```bash
uv run python -c 'from pathlib import Path; from neetcode_dashboard.backup import BackupArtifact, restore_verified_backup; from neetcode_dashboard.config import Settings; s=Settings(); a=BackupArtifact(Path("backups/backup-REPLACE.sqlite3"), Path("backups/backup-REPLACE.manifest.json")); print(restore_verified_backup(a, s.database_path))'
```

복원은 다음 중 하나라도 성립하면 실패하며 기존 DB를 바꾸지 않습니다.

- DB 또는 manifest의 SHA-256·revision·행 수·무결성 결과가 불일치
- 백업 파일 옆에 `-wal` 또는 `-shm` sidecar가 존재
- 복원 대상 DB 옆에 `-wal` 또는 `-shm` sidecar가 존재
- 실행 중인 앱이 복원 대상 DB의 프로세스 잠금을 보유
- 복원 대상으로 백업 원본 자체를 지정

## 전체 검증

```bash
uv run pytest --cov=neetcode_dashboard --cov-report=term-missing --cov-fail-under=90
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run alembic check
shasum -a 256 PLAN.md
git diff --check -- . ':!PLAN.md'
```

`PLAN.md`의 기대 SHA-256은 다음과 같습니다.

```text
1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96
```

`PLAN.md`에는 Markdown hard break를 위한 의도적인 trailing space가 있으므로, 일반 diff whitespace 검사는 이 파일만 제외합니다. 바이트 동일성은 별도 SHA-256 테스트가 보장합니다.

## Foundation이 보장하는 것

- 2026-08-06부터 2027-08-05까지 정확히 365일
- 기본 1,304시간, 공휴일 22개 적용 후 1,292시간
- 모든 앱 SQLite 연결에 `foreign_keys=ON`, WAL, `synchronous=FULL`, 5초 busy timeout, `recursive_triggers=ON`
- raw SQL의 이벤트 UPDATE/DELETE뿐 아니라 `INSERT OR REPLACE`·UPSERT 충돌도 차단하는 DB trigger
- 스트림별 연속 번호와 canonical JSON 기반 SHA-256 이벤트 체인
- SQLite backup API, `integrity_check`, revision·행 수·content hash·전체 이벤트 체인을 통과한 백업만 복원
- 앱과 복원 작업 사이의 interprocess lock 및 교체 직전 SQLite sidecar 재검사
- 요청마다 DB 상태와 이벤트 체인을 다시 검사하고 파일 경로나 비밀값을 노출하지 않는 loopback-only FastAPI UI
- 직접 ASGI 실행으로 외부 주소에 잘못 바인딩해도 비루프백 클라이언트 요청은 애플리케이션에서 거부
- 소스 checkout 밖에 설치한 wheel에서도 migration, startup, health, 백업 실행 가능

## 아직 보장하지 않는 것

Foundation은 문제를 스케줄하거나 채점하지 않습니다. NeetCode 문제 목록, P001–P080 콘텐츠, Codex 면접관 보정, 음성 입력, 애니메이션 생성·qualification은 후속 slice에서 각자 테스트와 승인 게이트를 통과한 뒤 활성화합니다.
