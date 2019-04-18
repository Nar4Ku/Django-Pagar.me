from django.contrib import admin
from django.urls import path
from home.views import test, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', test, name="test"),
    path('success/', success, name="success")
]
