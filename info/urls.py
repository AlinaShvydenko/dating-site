from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
 path('', views.main_page, name='main_page'),
 path('<str:name>', views.main_page),
 path('<str:name>/<str:color>', views.main_page),
 path('couples/', views.couples, name='couples'),
 path('forum/', views.forum, name='forum'),
 path('apply/', views.apply, name='apply'),
]
