from django.urls import path


from . import views

urlpatterns = [
    path('', views.AboutIndex.as_view()),
    path('name/', views.AboutName.as_view(), name='name'),
    path('basic/', views.AboutBasic.as_view(), name='basic'),
    path('episode/', views.AboutEpisode.as_view(), name='episode'),
    path('appeal/', views.AboutAppeal.as_view(), name='appeal'),
    path('email/', views.AboutEmail.as_view(), name='email'),
    path('api/', views.AboutViewSet.as_view({'get': 'list'})),
    path('api/<pk>', views.AboutViewSet.as_view({'get': 'retrieve'})),
]
