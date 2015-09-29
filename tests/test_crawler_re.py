from unittest import TestCase
import unittest

from main import crawler
from main import WIKI_PAGE


class TestCrawlerRe(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_crawler(self):
        craws = crawler(WIKI_PAGE, 1)

        n = sum(1 for i in craws)

        self.assertEqual(n, 1)
