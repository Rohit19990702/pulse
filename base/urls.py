from django.urls import path
from . import views
urlpatterns=[
    path('',views.intro,name="intro"),
    path('home/',views.home,name="home"),
    path('alerts/<str:pk>/',views.alerts,name="alerts"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]