from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
def about_detail(request, pk):
    """
    詳細を書き換えたり削除したりいろいろやる
    """
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AboutSerializer(about)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AboutSerializer(about, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        About.delete()
        return HttpResponse(status=204)
