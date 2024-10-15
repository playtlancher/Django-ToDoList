from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.loginHandler, name="login"),
    path("registration/", views.registrationHandler, name="registration"),
    path("", views.loginHandler),
    path("home/", views.home),
]
