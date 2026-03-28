"""Seed a starter list of liquid US tickers (MVP helper)."""

STARTER_TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "AMD",
    "AMZN",
    "META",
    "GOOGL",
]


if __name__ == "__main__":
    print("seed tickers:", ",".join(STARTER_TICKERS))
