from unittest import TestCase
import unittest

from main import get_browser, get_paragraph


class TestCrawler(TestCase):

    def setUp(self):
        self.browser = get_browser()

    def test_crawler(self):
        self.assertIsNotNone(self.browser)

    def test_page(self):
        paragraph = get_paragraph(self.browser)
        self.assertIsNotNone(paragraph)
        self.assertIsInstance(paragraph, unicode)

    def tearDown(self):
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
