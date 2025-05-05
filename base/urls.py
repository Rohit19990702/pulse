from django.urls import path
from . import views
urlpatterns=[
    path('',views.intro,name="intro"),
    path('home/',views.home,name="home"),
    path('alerts/<str:pk>/',views.alerts,name="alerts"),
]