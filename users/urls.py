from rest_framework.routers import DefaultRouter
from . import views
from .apps import UsersConfig
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', views.UserModelViewSet, basename='user')
urlpatterns = [
    #  user tokens
    path('api-token-auth/', obtain_auth_token, name='token_obtain'),
] + router.urls
