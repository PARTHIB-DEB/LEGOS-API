from APP import views
from django.urls import path

urlpatterns = [
    path("lego",views.legolist.as_view()),
    path("login",views.login),
]