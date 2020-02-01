from loguru import logger

from link_scraper import LinkScraper


def main():
    logger.disable("link_scraper")
    link_Scrapper = LinkScraper()
    link_Scrapper.print_links()


if __name__ == "__main__":
    main()
