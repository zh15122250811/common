from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^mineindex/',views.mineIndex,name="mineindex"),
    url(r'^register/',views.register,name="register"),
    url(r'^logout/',views.logout,name="logout"),
    url(r'^check_user/',views.check_user,name="check_user"),
    url(r'^login/',views.login,name="login"),
]