from rest_framework import serializers

from transportation_suppliers.users.models import User, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "address1",
            "address2",
            "area",
            "city",
            "county",
            "postcode",
            "country",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    addresses_nested = AddressSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "name",
            "avatar",
            "bio",
            "salutation",
            "gender",
            "date_joined",
            "addresses_nested",
        ]
        extra_kwargs = {
            "date_joined": {"read_only": True},
            "username": {"read_only": True},
            "first_name": {"read_only": True},
            "last_name": {"read_only": True},
            "name": {"read_only": True},
            "avatar": {"read_only": True},
            "bio": {"read_only": True},
            "salutation": {"read_only": True},
            "gender": {"read_only": True},
        }


class SimpleUserSerializer(serializers.ModelSerializer):
    addresses_nested = AddressSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "name",
            "email",
            "avatar",
            "bio",
            "salutation",
            "date_of_birth",
            "gender",
            "phone_home",
            "phone_work",
            "mobile",
            "date_joined",
            "addresses_nested",
        ]
        extra_kwargs = {"date_joined": {"read_only": True}}


class UserSerializer(serializers.ModelSerializer):
    addresses = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), many=True, write_only=True
    )
    addresses_nested = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "name",
            "email",
            "avatar",
            "bio",
            "salutation",
            "date_of_birth",
            "gender",
            "phone_home",
            "phone_work",
            "mobile",
            "date_joined",
            "addresses",
            "addresses_nested",
        ]
        extra_kwargs = {"date_joined": {"read_only": True}}
