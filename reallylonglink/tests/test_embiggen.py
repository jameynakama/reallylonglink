from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

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

    def test_embiggen_generates_2000_char_string(self):
        """`rll.embiggen()` should generate a 1999 character long string"""
        expected_length = settings.REALLY_LONG_LINK_LENGTH
        self.rll.embiggen()
        assert len(self.rll.long_link) == expected_length
