# Pump Pattern Research & Scanner

Production-oriented MVP scaffold for a **Pump Pattern Research & Scanner** service:

- historical daily OHLCV ingestion,
- x2+ pump event detection,
- pre-pump feature extraction,
- live similarity scan and ranking.

## Monorepo layout

```text
apps/
  api/
  worker/
packages/
  core/
  db/
  schemas/
scripts/
tests/
```

## Quick start

1. Create `.env` from `.env.example`.
2. Start infra:
   ```bash
   docker compose up -d postgres redis
   ```
3. Install dependencies:
   ```bash
   pip install -e .[dev]
   ```
4. Run API:
   ```bash
   uvicorn apps.api.main:app --host 0.0.0.0 --port 8000 --reload
   ```
5. Open `http://localhost:8000/health`.

## Railway services

- `api`: `uvicorn apps.api.main:app --host 0.0.0.0 --port $PORT`
- `worker-ingest`: `python apps/worker/ingest_worker.py`
- `worker-analysis`: `python apps/worker/analysis_worker.py`
- `cron-daily`: `python scripts/run_daily_scan.py`

Managed dependencies:
- PostgreSQL
- Redis

## Current scope (MVP constraints)

- US stocks only
- daily timeframe only
- EOD batch scan
- initial universe: 500-800 tickers
- no minute bars, no realtime alerts


## Build & validation commands

```bash
make build   # bytecode compilation check for apps/packages/scripts
make test    # pytest
make run     # local API run
```

> Note: in restricted environments without package index access, `make build` works offline, while `make test` may require preinstalled dependencies.


### Internet connectivity check

```bash
python scripts/check_internet.py
```

Use this helper to diagnose DNS/HTTPS access when running inside restricted CI/container environments.


### Deploy to `main`

```bash
bash scripts/deploy_main.sh
```

This helper switches to `main`, runs build/tests, and pushes `main` if remote `origin` is configured.
