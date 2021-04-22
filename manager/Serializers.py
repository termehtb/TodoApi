from rest_framework import serializers

from user.models import User
from user.serializers import UserSerializer
from userprofile.models import UserProfile


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'first_name', 'last_name', 'phone_number', 'age', 'gender')


class AdminRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_superuser(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender']
        )
        return user
