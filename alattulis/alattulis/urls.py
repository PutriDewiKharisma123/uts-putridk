
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pensil/', include('pensil.urls')),
    path('buku/', include('buku.urls')),
    path('penghapus/', include('penghapus.urls')),
]
