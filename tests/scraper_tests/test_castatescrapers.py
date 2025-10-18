'''Tests for CA state scrapers'''
import unittest, re

from scrapers import ca_senate_scraper, ca_assembly_scraper


class TestCAAssemblyScraper(unittest.TestCase):
    """Tests for CA Assembly scraper"""

    def test_get_assembly_members(self):
        """
        Checks if list of CA assembly members equal to 80, number on CA state assembly website.
        """
        assembly_members = ca_assembly_scraper.get_members()

        self.assertTrue(isinstance(assembly_members, list))
        self.assertEqual(len(assembly_members), 80)
        for member in assembly_members:
            self.assertIn("last_name", member)
            self.assertIn("first_name", member)
            self.assertIn("party", member)
            self.assertIn("district_number", member)


# class TestCASenateScraper(unittest.TestCase):
#     """Tests for CA senate scraper."""

#     def test_get_senators(self):
#         """
#         Checks if list of CA senators equal to 40, number on CA state assembly website.
#         """
#         senators = ca_senate_scraper.get_senators()

#         self.assertTrue(isinstance(senators, list))
#         self.assertEquals(len(senators), 40)
