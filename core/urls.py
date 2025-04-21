from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse('<h1>Ola Mundo</h1>')),
]


