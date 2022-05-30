from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from financepeer_app.models import Usersdata, Users
from financepeer_app.serializers import UsersdataSerializer
import json
@api_view(['POST'])
def load_data(request):
    user = Users.objects.get(username=request.data['user'])
    if not user.login_flag:
        return Response({"message": "unauthorized user"}, status=status.HTTP_400_BAD_REQUEST)
    file = request.FILES['file']
    extension = str(file).split('.')[1]
    if extension != 'json':
        return Response({"message": "invalid format"}, status=status.HTTP_400_BAD_REQUEST)
    json_data = json.loads(file.read())
    for data in json_data:
        data['userid'] = data['userId']
        data['body'] = data['body'].replace('\n', ' ')
        serializer = UsersdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "data saved successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def view_data(request):
    user = Users.objects.get(username=request.data['user'])
    if not user.login_flag:
        return Response({"message": "unauthorized user"}, status=status.HTTP_400_BAD_REQUEST)
    userdata = Usersdata.objects.all()
    serializer = UsersdataSerializer(userdata, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)