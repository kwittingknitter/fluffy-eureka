'''Tests for CA state scrapers'''
import unittest

from scrapers import ca_senate_scraper, ca_assembly_scraper


class TestCAAssemblyScraper(unittest.TestCase):
    """Tests for CA Assembly scraper"""

    def test_get_assembly_members(self):
        """
        Checks if list of CA assembly members equal to 80, number on CA state assembly website.
        """
        assembly_members = ca_assembly_scraper.get_members()

        self.assertIsInstance(assembly_members, list)
        self.assertEqual(len(assembly_members), 80)
        for member in assembly_members:
            self.assertIn("last_name", member)
            self.assertIn("first_name", member)
            self.assertIn("party", member)
            self.assertIn("district_number", member)
            self.assertIsInstance(member["district_number"], int)


class TestCASenateScraper(unittest.TestCase):
    """Tests for CA senate scraper."""

    def test_get_senators(self):
        """
        Checks if list of CA senators equal to 40, number on CA state assembly website.
        """
        senators = ca_senate_scraper.get_senators()

        self.assertIsInstance(senators, list)
        self.assertEqual(len(senators), 40)
        for senator in senators:
            self.assertIn("last_name", senator)
            self.assertIn("first_name", senator)
            self.assertIn("party", senator)
            self.assertIn("district_number", senator)
            self.assertIsInstance(senator["district_number"], int)

    def test_get_senate_comms(self):
        """
        Checks list of CA senate committees
        """
        committees = ca_senate_scraper.get_committees()

        self.assertIsInstance(committees, list)
        self.assertGreater(len(committees), 0)
        for comm in committees:
            self.assertIn("name", comm)
            self.assertIn("committee_type", comm)
