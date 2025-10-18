import re

from bs4 import BeautifulSoup

from .scraper import BaseScraper


class CAStateSenateScraper(BaseScraper):
    """
    Scrapes CA senate website
    """
    BASE_URL = 'https://www.senate.ca.gov/'
    SENATORS_ENDPOINT = 'senators'
    COMMITTEES_ENDPOINT = 'committees'

    def __init__(self):
        """
        Initializes scraper.
        """
        super().__init__(self.BASE_URL)

    def get_senators(self):
        """
        Gets senators,

        Returns list of dict with info about each senator.
        """
        response = self.session.get(self.BASE_URL+self.SENATORS_ENDPOINT)
        soup = BeautifulSoup(response.content, "html.parser")
        members_data = soup.find_all(class_="page-members__member")
        members = []
        for member_info in members_data:
            info = [c for c in member_info.contents]
            name_and_party = re.split(r'\W+', info[0].next_sibling.text)
            members.append({
                "first_name": name_and_party[0],
                "last_name": name_and_party[1],
                "district_number": int(re.search(r"\d+", info[2].text).group()),
                "party": "Democrat" if "D" in name_and_party[2] else "Republican",
            })
        return members

    def get_committees(self):
        """
        Gets senate committees.

        Returns list.
        """
        pass
        # response = self.session.get(self.BASE_URL+self.COMMITTEES_ENDPOINT)


class CAStateAssemblyScraper(BaseScraper):
    """
    Scrapes CA state assembly website
    """
    BASE_URL = 'https://www.assembly.ca.gov/'
    ASSEMBLYMEMBERS_ENDPOINT = 'assemblymembers'
    COMMITTEES_ENDPOINT = 'committees'

    def __init__(self):
        """
        Initializes scraper.
        """
        super().__init__(self.BASE_URL)

    def get_members(self):
        """
        Gets assembly members.

        Returns a list of dict with info about each member.
        """
        response = self.session.get(self.BASE_URL+self.ASSEMBLYMEMBERS_ENDPOINT)
        soup = BeautifulSoup(response.content, "html.parser")
        members_data = soup.find_all(class_="members-list__content")
        members = []
        for member_info in members_data:
            info = [c.text for c in member_info]
            name = re.split(r'\W+', info[0])
            members.append({
                "last_name": name[0],
                "first_name": name[1],
                "district_number": int(re.search(r"\d+", info[1]).group()),
                "party": info[2]
            })
        return members
    

    def get_committees(self):
        """
        Gets committees.

        Returns a list of assembly committees.
        """
        pass
        # response = self.session.get(self.BASE_URL+self.COMMITTEES_ENDPOINT)


class CALegInfoScraper(BaseScraper):
    """
    Scrapes CA bill info website.

    """
    BASE_URL = 'https://leginfo.legislature.ca.gov/'
    BILLSEARCH_ENDPOINT = 'faces/billSearchClient.xhtml'

    def __init__(self):
        super().__init__(self.BASE_URL)
