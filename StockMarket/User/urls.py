from django.urls import path
from .views import CreateUserView, RetrieveUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("create/", CreateUserView.as_view()),
    path("<int:pk>", RetrieveUser.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
