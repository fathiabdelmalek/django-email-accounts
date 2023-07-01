from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'url')
