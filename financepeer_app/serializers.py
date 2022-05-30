from rest_framework import serializers
from financepeer_app.models import Users, Usersdata

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class UsersdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersdata
        fields = "__all__"