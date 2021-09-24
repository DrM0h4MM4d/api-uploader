from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Users
from .validators import validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Users.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Users
        fields = ('username', 'password', 'password2', 'email', 'phone_number', 'why_using', 'job', 'region')


    def validate(self, attrs):
        if attrs['passowrd'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'passwords didn\'t match'})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['pk', 'profile_picture', 'username', 'first_name', 
                    'last_name', 'phone_number', 'about', 
                    'why_using', 'job', 'region', 'last_login',
                ]
        