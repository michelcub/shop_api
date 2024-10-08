from rest_framework.serializers import ModelSerializer

from ..models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

        def create(self, validated_data):
            user = User()
            user.username = validated_data["username"]
            user.email = validated_data["email"]
            user.set_password(validated_data["password"])

            user.save()

            return user
