from django.contrib import admin
from django.urls import path, include

from app_casinos import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("aa1/",  views.index, name="index"),
    path("", admin.site.urls),
    # path("111/", include("app_casinos.urls")),


]
