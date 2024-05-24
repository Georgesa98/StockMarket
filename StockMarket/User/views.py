from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from .models import User

from .serializer import CreateUserSer, GetUserSer


# Create your views here.
class CreateUserView(APIView):
    def post(self, request):
        try:
            serializer = CreateUserSer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveUser(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = GetUserSer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        pass
