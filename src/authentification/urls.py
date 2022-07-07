from django.urls import path
from authentification.views import Login, SignUp, logout_view

app_name = "authentification"


urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', logout_view, name="logout"),

]
