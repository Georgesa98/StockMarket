from django.urls import path
from .views import Deposit, Transact

urlpatterns = [
    path("deposit/", Deposit.as_view()),
    path("", Transact.as_view()),
]
