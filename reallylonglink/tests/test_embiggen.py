import re

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from reallylonglink.models import ReallyLongLink


class TestEmbiggen(TestCase):
    def setUp(self):
        self.rll = ReallyLongLink.objects.create(original_link='http://example.com')

    def test_form_generates_long_link(self):
        """POSTing to /home/ should generate a really long link"""
        expected_long_links = ReallyLongLink.objects.count() + 1
        data = {'original_link': 'http://example.com'}
        self.client.post(reverse('home'), data=data)
        assert ReallyLongLink.objects.count() == expected_long_links

    def test_embiggen_generates_long_link(self):
        """`rll.embiggen()` should generate a long string"""
        expected_length = settings.REALLY_LONG_LINK_LENGTH
        self.rll.embiggen()
        assert len(self.rll.long_link) == expected_length

    def test_never_allow_double_slashes(self):
        """`rll.embiggen()` should never allow two consecutive slashes"""
        expected_link = re.compile(r'hello/[\w\d]moto')
        rll = ReallyLongLink.objects.create(original_link='something', long_link='hello//moto')
        assert expected_link.match(rll.long_link)

    def test_never_allow_long_link_to_begin_with_slash(self):
        """`rll.embiggen()` should never allow links to begin with slashes"""
        expected_link = re.compile(r'[\w\d]hello/moto')
        rll = ReallyLongLink.objects.create(original_link='something', long_link='/hello/moto')
        assert expected_link.match(rll.long_link)

    def test_never_allow_long_link_to_end_with_slash(self):
        """`rll.embiggen()` should never allow links to end with slashes"""
        expected_link = re.compile(r'hello/moto[\w\d]')
        rll = ReallyLongLink.objects.create(original_link='something', long_link='hello/moto/')
        assert expected_link.match(rll.long_link)
