import logging

from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView, RedirectView

from reallylonglink.forms import ReallyLongLinkForm
from reallylonglink.models import ReallyLongLink


logger = logging.getLogger(__name__)


class HomeView(FormView):
    template_name = 'reallylonglink/home.html'
    form_class = ReallyLongLinkForm
    success_url = '/'

    def form_valid(self, form):
        original_link = form.cleaned_data['original_link']
        rll = ReallyLongLink.objects.create(original_link=original_link)
        rll.embiggen()
        return HttpResponseRedirect(reverse('generated_link', kwargs={'pk': rll.pk}))


class RLLRedirectView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        long_link = kwargs['long_link']
        rll = get_object_or_404(ReallyLongLink, long_link=long_link)
        logger.info("Redirecting to {}".format(rll.long_link))
        return rll.original_link


def generated_link_view(request, pk=None):
    # TODO: TEST
    rll = get_object_or_404(ReallyLongLink, pk=pk)
    protocol = 'https' if request.is_secure() else 'http'
    context = {
        'original_link': rll.original_link,
        'really_long_link': '{}://{}{}/{}'.format(protocol, request.get_host(),
                                                  '/' + settings.BASE_REDIRECT_URL, rll.long_link)
    }
    return render(request, 'reallylonglink/reallylonglink.html', context)
