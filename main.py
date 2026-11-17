import argparse
import statistics
import time

import requests


BITS_IN_BYTE = 8
BITS_IN_MEGABIT = 1_000_000


def add_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Скрипт скачивает контент по ссылке",
    )
    parser.add_argument(
        "--url",
        help="url по которому можно скачать контент",
        required=True,
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Таймаут запроса, по умолчанию 10 секунд",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Сколько раз будет скачан контент по ссылке, по умолчанию 10",
    )
    return parser


def fetch_url(url: str, timeout: float) -> tuple[float, float]:
    start = time.perf_counter()
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    content = response.content
    dowloaded = len(content)
    counter = time.perf_counter() - start
    return counter, dowloaded


def main() -> None:
    parser = add_argument_parser()
    args = parser.parse_args()
    url = args.url
    count = args.count
    timeout = args.timeout
    counters = []
    total_downloaded = 0
    try:
        print("Start download content.")
        for _ in range(count):
            counter, dowloaded = fetch_url(url=url, timeout=timeout)
            counters.append(counter)
            total_downloaded += dowloaded
        avg_counter = statistics.mean(counters)
        speed = (
            total_downloaded * BITS_IN_BYTE / (avg_counter * count) / BITS_IN_MEGABIT
        )
        print(f"Download speed - {speed:.5f} Mbit/s")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
