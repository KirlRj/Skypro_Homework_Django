from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView, LoginView

from users.forms import UserLoginForm

app_name = "users"

urlpatterns = [
    path("register/", views.CreateNewUserView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:home"), name="logout"),
]
