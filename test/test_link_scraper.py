from link_scraper import LinkScraper


def test_link_scraper() -> None:
    link_scraper = LinkScraper()
    assert link_scraper.get_links(depth=0) == {
        "url": "http://www.blankwebsite.com/",
        "urls": [],
    }
    assert link_scraper.get_links(depth=1) == {
        "url": "http://www.blankwebsite.com/",
        "urls": [{"url": "http://www.pointlesssites.com/", "urls": []}],
    }
