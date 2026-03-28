from packages.core.logging import configure_logging


def main() -> None:
    configure_logging(service_name="worker-analysis")
    print("analysis worker started (MVP stub)")


if __name__ == "__main__":
    main()
