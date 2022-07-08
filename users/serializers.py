from rest_framework import serializers
from .models import Users
from bocr_api.common.datetime import DateTime
from bocr_api.common.utils import Utils


class RegisterSerializer(serializers.ModelSerializer):
    __utils = Utils()

    class Meta:
        model = Users
        fields = ["name", "email", "password"]

    def create(self, validated_data):
        validated_data["password"] = self.__utils.hash_password(
            validated_data["password"])
        user: Users = Users.objects.create(**validated_data)
        user.verification_token = self.__utils.encrypt({
            "email":
            user.email,
            "name":
            user.name,
            "profile_pic":
            user.profile_pic,
            "cover_pic":
            user.cover_pic,
            "is_active":
            user.is_active
        })
        user.verification_token_generated_at = DateTime.now()
        user.save()
        return user