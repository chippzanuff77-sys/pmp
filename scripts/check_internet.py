"""Simple internet connectivity diagnostic for restricted environments."""

from __future__ import annotations

import socket
import ssl
from urllib.parse import urlparse

import urllib.request

TEST_URLS = [
    "https://example.com",
    "https://www.google.com",
]


def check_dns(hostname: str) -> tuple[bool, str]:
    try:
        ip = socket.gethostbyname(hostname)
        return True, ip
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def check_https(url: str, timeout: int = 10) -> tuple[bool, str]:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as resp:
            return True, f"HTTP {resp.status}"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def main() -> int:
    status = 0
    for url in TEST_URLS:
        host = urlparse(url).hostname or ""
        ok_dns, dns_result = check_dns(host)
        print(f"[DNS] {host}: {'OK' if ok_dns else 'FAIL'} ({dns_result})")

        ok_https, https_result = check_https(url)
        print(f"[HTTPS] {url}: {'OK' if ok_https else 'FAIL'} ({https_result})")

        if not (ok_dns and ok_https):
            status = 1

    return status


if __name__ == "__main__":
    raise SystemExit(main())
