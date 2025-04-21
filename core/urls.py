from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse('<h1 style="color: indigo;font-size: 50px;font-family: Arial, Helvetica, sans-serif;text-align: center;text-decoration: underline;text-transform: uppercase;">Ola Mundo</h1>')),
]