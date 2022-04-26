from django.contrib.auth import logout
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
  
]