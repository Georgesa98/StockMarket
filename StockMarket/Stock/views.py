from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from Stock.models import Stock

from .serializer import CreateStockSer, GetStockSer


# Create your views here.
class CreateStockView(APIView):
    def post(self, request):
        try:
            serializer = CreateStockSer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveStockView(APIView):
    def get(self, request, symbol):
        try:
            stock = Stock.objects.get(symbol=symbol)
            serializer = GetStockSer(stock)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_404_NOT_FOUND)


class GetAllStockSymbols(APIView):
    def get(self, request):
        try:
            stocks = Stock.objects.all()
            symbols = []
            for stock in stocks:
                symbols.append({"symbol": stock.symbol, "company_name": stock.co_name})
            return Response(symbols, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_404_NOT_FOUND)
