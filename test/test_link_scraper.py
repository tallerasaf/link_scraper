from link_scraper import link_scraper


def test_fib() -> None:
    assert link_scraper.fib(0) == 0
    assert link_scraper.fib(1) == 1
    assert link_scraper.fib(2) == 1
    assert link_scraper.fib(3) == 2
    assert link_scraper.fib(4) == 3
    assert link_scraper.fib(5) == 5
    assert link_scraper.fib(10) == 55
