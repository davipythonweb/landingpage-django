from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from home import views as home_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('blog/', blog_views.blog, name='blog'),
    path('teste/', lambda request: HttpResponse('<h1 style="color: indigo;font-size: 50px;font-family: Arial, Helvetica, sans-serif;text-align: center;text-decoration: underline;text-transform: uppercase;">Ola Mundo</h1>')),
]