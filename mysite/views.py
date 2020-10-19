from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exemhttps://www.nicovideo.jp/tag/%E3%81%9B%E3%81%8C%E3%81%9F%E4%B8%89%E5%9B%9B%E9%83%8Ept
from rest_framework.parsers import JSONParser
from mysite.models import About
from mysite.serializers import AboutSerializer

# Create your views here.


@csrf_exempt
def about_list(request):
    """
    すべてのAboutをリストで表示したりする。
    """
    if request.method == 'GET':
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def about_detail(request):
    pass

