from typing import Any, Dict, List, Sequence

from loguru import logger
from requests_html import HTMLSession

from .config import DEFAULT_DEPTH, DEFAULT_URL
from .utils import get_pretty_json


class LinkScraper:
    def __init__(self):
        logger.info("Initialize a new LinkScraper")
        self.session = HTMLSession()

    def print_links(self, url: str = DEFAULT_URL, depth: int = DEFAULT_DEPTH) -> None:
        logger.info(f"Starting to print links. {url=}, {depth=}")
        links_map = self.get_links(url, depth)
        print(get_pretty_json(links_map))

    def get_links(
        self, url: str = DEFAULT_URL, depth: int = DEFAULT_DEPTH
    ) -> Dict[str, Sequence[Any]]:
        try:
            logger.info(f"Starting to get links. {url=}, {depth=}")
            return self.get_links_recursively(url, depth)
        except Exception:
            logger.exception(f"Failed to get links. {url=}, {depth=}")
            return {"url": url, "urls": []}

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
            logger.trace(f"Starting to get a webpage. {url=}")
            r = self.session.get(url)
            links = r.html.absolute_links
        except Exception:
            logger.warning(f"Failed to get links. {url=}")
            return []
        else:
            logger.trace(f"Successfully get links from webpage. {url=}")
            return list(links)
