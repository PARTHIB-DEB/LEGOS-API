from APP import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lego',views.legoViewSet,basename='legolist') # Can go to this url by NEW TAB 
urlpatterns = router.urls

urlpatterns = [
    path("",include(router.urls)),
    path("lego",views.legolist.as_view()), #Can go this url in SAME TAB
    path("login",views.login),
    path("register",views.registers),
]