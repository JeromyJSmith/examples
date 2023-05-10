from typing import Any

from bs4 import BeautifulSoup


def get_from_bs(soup: BeautifulSoup, key: str, default: Any = None) -> Any | None:
    return value.get_text() if (value := soup.find(key)) else default
