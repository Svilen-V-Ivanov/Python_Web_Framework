from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as validators
from django.core import exceptions
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    # This hashes the password
    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    # This invokes the password validators
    def validate(self, data):
        # Invoke password validators
        user = UserModel(**data)
        password = data.get('password')
        errors = {}

        try:
            validators.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)

    # This removes password from the response
    def to_representation(self, instance):
        user_representation = super().to_representation(instance)
        user_representation.pop('password')

        return user_representation
