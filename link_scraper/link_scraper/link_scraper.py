from typing import Any, Dict, List, Sequence

from requests_html import HTMLSession

from .config import DEFAULT_DEPTH, DEFAULT_URL
from .utils import get_pretty_json


class LinkScraper:
    def __init__(self):
        self.session = HTMLSession()

    def print_links(self, url: str = DEFAULT_URL, depth: int = DEFAULT_DEPTH) -> None:
        links_map = self.get_links(url, depth)
        print(get_pretty_json(links_map))

    def get_links(
        self, url: str = DEFAULT_URL, depth: int = DEFAULT_DEPTH
    ) -> Dict[str, Sequence[Any]]:
        return self.get_links_recursively(url, depth)

    def get_links_recursively(
        self, url: str, depth: int, step: int = 0
    ) -> Dict[str, Sequence[Any]]:
        inner_links: List[Any] = []
        links_map = {"url": url, "urls": inner_links}
        if step == depth:
            return links_map
        for link in self._get_links_from_page(url):
            inner_links.append(self.get_links_recursively(link, depth, step + 1))
        return links_map

    def _get_links_from_page(self, url: str) -> List[str]:
        try:
            r = self.session.get(url)
            links = r.html.absolute_links
        except Exception:
            return []
        else:
            return list(links)
