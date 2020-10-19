from django.urls import path


from . import views

urlpatterns = [
    path('', views.about_list),
    path('<int:pk>/', views.about_detail),
]