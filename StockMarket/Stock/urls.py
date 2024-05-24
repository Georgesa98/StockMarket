from django.urls import path, re_path
from .views import CreateStockView, RetrieveStockView, GetAllStockSymbols
from .consumer import StockConsumer

urlpatterns = [
    path("create/", CreateStockView.as_view()),
    path("<str:symbol>", RetrieveStockView.as_view()),
    path("symbols/", GetAllStockSymbols.as_view()),
]
websocket_urlpatterns = [re_path(r"ws/", StockConsumer.as_asgi())]
