from django.urls import path
from . import views

urlpatterns = [
 path('', views.main_page, name='main_page'),
 path('<str:name>/<str:color>', views.main_page),
 path('couples/', views.couples, name='couples'),
 path('forum/', views.forum, name='forum'),
 path('apply/', views.apply, name='apply'),
 path('applications_display/', views.applications_display, name='applications_display'),
 path('accepted/', views.create_club_member, name='create_club_member'),
]
