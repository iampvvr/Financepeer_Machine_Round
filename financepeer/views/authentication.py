from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from financepeer_app.models import Users
from financepeer_app.serializers import UsersSerializer
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = request.data
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "data saved successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = Users.objects.get(username=data['username'])
        except:
            return Response({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
        if user.password != data['password']:
            return Response({"message": "incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
        data['login_flag'] = True
        serializer = UsersSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user logged in successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = Users.objects.get(username=data['username'])
        except:
            return Response({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
        if not user.login_flag:
            return Response({"message": "user already logged out"}, status=status.HTTP_400_BAD_REQUEST)
        data['login_flag'] = False
        serializer = UsersSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user logged out successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)