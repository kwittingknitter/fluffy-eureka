import requests


class BaseScraper:
    """Base Scraper class"""
    BASE_URL = ''
    HEADERS = {'User-Agent': 'Mozilla/5.0'}

    def __init__(self, url):
        """
        Initializes scraper.
        """
        self.BASE_URL = url
        self.session = requests.Session()
