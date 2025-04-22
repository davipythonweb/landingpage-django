from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),

    path('teste/', lambda request: HttpResponse('<h1 style="color: indigo;font-size: 50px;font-family: Arial, Helvetica, sans-serif;text-align: center;text-decoration: underline;text-transform: uppercase;">Ola Mundo</h1>')),
]