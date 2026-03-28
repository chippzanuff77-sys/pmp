from datetime import datetime, timezone


if __name__ == "__main__":
    now = datetime.now(timezone.utc).isoformat()
    print(f"daily scan pipeline started at {now}")
