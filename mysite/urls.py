from django.urls import path


from . import views

urlpatterns = [
    path('', views.AboutViewSet.as_view()),
]
