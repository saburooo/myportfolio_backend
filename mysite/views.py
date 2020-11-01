from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mysite.models import About
from mysite.serializers import AboutSerializer

from rest_framework import viewsets

from django.views.generic import TemplateView


# Create your views here.


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    """ AboutモデルのCRUD用APIクラス、ただし、read only """
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutIndex(TemplateView):
    template_name = 'mysite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.get(id='1')
        return context


class AboutName(TemplateView):
    template_name = 'mysite/name.html'


class AboutBasic(TemplateView):
    template_name = 'mysite/basic.html'


class AboutEpisode(TemplateView):
    template_name = 'mysite/episode.html'


class AboutAppeal(TemplateView):
    template_name = 'mysite/appeal.html'


# Emailはフォームになるかもしれない。
class AboutEmail(TemplateView):
    template_name = 'mysite/email.html'

