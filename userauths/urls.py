from django.urls import path, include
from .views import *

app_name='userauths'

urlpatterns = [
    path('sign-up/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),

]