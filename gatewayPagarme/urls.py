from django.contrib import admin
from django.urls import path
from home.views import test, success, notification
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('logout', logout_view, name="logout"),
    path('sign-up/', register_view, name="sign_in"),
    path('home/', test, name="test"),
    path('success/', success, name="success"),
    path('post-back/', notification, name="notification")
]
