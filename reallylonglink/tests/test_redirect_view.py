from django.test import TestCase
from django.urls import reverse

from reallylonglink import models


class TestRedirectView(TestCase):
    def setUp(self):
        self.rll = models.ReallyLongLink.objects.create(
            original_link="http://example.com/"
        )
        self.rll.embiggen()

    def test_redirection(self):
        """The `rll.long_link` should redirect to `rll.oringial_link`"""
        expected_destination = self.rll.original_link
        expected_status_code = 301  # permanent
        response = self.client.get(
            reverse("redirect", kwargs={"long_link": self.rll.long_link})
        )
        self.assertRedirects(
            response,
            expected_destination,
            expected_status_code,
            fetch_redirect_response=False,
        )

    def test_no_rll_found(self):
        """The request should 404 if no rll is found"""
        expected_status_code = 404
        response = self.client.get(
            reverse("redirect", kwargs={"long_link": "nowayjose"})
        )
        assert response.status_code == expected_status_code
