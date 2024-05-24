from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from Stock.models import Stock

from .serializer import CreateTransactionSer
from User.models import User


# Create your views here.
class Deposit(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            amount = float(request.data["amount"])
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            user.balance += amount
            user.save()
            return Response(
                {"message": "deposit successfully", "balance": user.balance},
                status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class Transact(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = CreateTransactionSer(data=request.data)
            # request.data["user"] = request.user.id
            stock = Stock.objects.get(id=request.data["stock"])
            user = User.objects.get(id=request.data["user"])
            amount = request.data["quantity"] * stock.last_price
            request.data["amount"] = amount
            if serializer.is_valid():
                if user.balance > amount:
                    serializer.save()
                    return Response(serializer.data, status.HTTP_200_OK)
                else:
                    return Response(
                        {"message": "you need to deposit more money"},
                        status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
