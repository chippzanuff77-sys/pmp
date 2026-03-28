from datetime import date, datetime

from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from packages.db.models.base import Base


class PumpEvent(Base):
    __tablename__ = "pump_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker_id: Mapped[int] = mapped_column(ForeignKey("tickers.id"), index=True)
    base_date: Mapped[date] = mapped_column(Date)
    trigger_date: Mapped[date] = mapped_column(Date)
    peak_date: Mapped[date] = mapped_column(Date)
    base_price: Mapped[float] = mapped_column(Float)
    peak_price: Mapped[float] = mapped_column(Float)
    gain_pct: Mapped[float] = mapped_column(Float)
    duration_days: Mapped[int] = mapped_column(Integer)
    volume_confirmation: Mapped[float] = mapped_column(Float, default=0)
    quality_score: Mapped[float] = mapped_column(Float, default=0)
    detection_version: Mapped[str] = mapped_column(String(32), default="v1")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class FeatureSnapshot(Base):
    __tablename__ = "feature_snapshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker_id: Mapped[int] = mapped_column(ForeignKey("tickers.id"), index=True)
    reference_date: Mapped[date] = mapped_column(Date, index=True)
    event_id: Mapped[int | None] = mapped_column(ForeignKey("pump_events.id"), nullable=True)
    snapshot_type: Mapped[str] = mapped_column(String(32), index=True)

    ret_3d: Mapped[float | None] = mapped_column(Float, nullable=True)
    ret_5d: Mapped[float | None] = mapped_column(Float, nullable=True)
    ret_10d: Mapped[float | None] = mapped_column(Float, nullable=True)
    ret_20d: Mapped[float | None] = mapped_column(Float, nullable=True)
    rv_5d: Mapped[float | None] = mapped_column(Float, nullable=True)
    rv_20d: Mapped[float | None] = mapped_column(Float, nullable=True)
    atr_pct: Mapped[float | None] = mapped_column(Float, nullable=True)
    volatility_10d: Mapped[float | None] = mapped_column(Float, nullable=True)
    range_compression_10d: Mapped[float | None] = mapped_column(Float, nullable=True)
    breakout_distance_20d: Mapped[float | None] = mapped_column(Float, nullable=True)
    rsi_14: Mapped[float | None] = mapped_column(Float, nullable=True)
    sma20_distance: Mapped[float | None] = mapped_column(Float, nullable=True)
    sma50_distance: Mapped[float | None] = mapped_column(Float, nullable=True)
    high_20_breakout_flag: Mapped[float | None] = mapped_column(Float, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class ScanRun(Base):
    __tablename__ = "scan_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    run_type: Mapped[str] = mapped_column(String(32), index=True)
    status: Mapped[str] = mapped_column(String(32), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    tickers_scanned: Mapped[int] = mapped_column(Integer, default=0)
    events_found: Mapped[int] = mapped_column(Integer, default=0)
    notes_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)


class ScanResult(Base):
    __tablename__ = "scan_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("scan_runs.id"), index=True)
    ticker_id: Mapped[int] = mapped_column(ForeignKey("tickers.id"), index=True)
    reference_date: Mapped[date] = mapped_column(Date, index=True)
    final_score: Mapped[float] = mapped_column(Float)
    similarity_score: Mapped[float] = mapped_column(Float)
    matched_event_count: Mapped[int] = mapped_column(Integer, default=0)
    top_pattern_family: Mapped[str | None] = mapped_column(String(64), nullable=True)
    explanation_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
