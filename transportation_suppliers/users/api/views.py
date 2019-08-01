from transportation_suppliers.users.models import User, Address
from transportation_suppliers.users.api import serializers


from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    # Manage Personal Details.

    User can only list, get, retrieve, update and destroy his own personal
    details.
    """

    queryset = User.objects.all().order_by("-date_joined")

    def get_serializer_class(self):
        if self.request.version == "v1":
            return serializers.SimpleUserSerializer
        return serializers.UserSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                return self.queryset.filter(id=self.request.user.id)
            except Exception:
                return self.queryset.none()
        else:
            return self.queryset.none()


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    # View user profiles.

    User can list profiles and get their details using the usernames.
    """

    queryset = User.objects.all().order_by("-date_joined")

    lookup_field = "username"
    lookup_url_kwarg = "username"

    def get_serializer_class(self):
        if self.request.version == "v1":
            return serializers.SimpleProfileSerializer
        return serializers.ProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    # Manage addresses.
    """

    queryset = Address.objects.all().order_by("-id")
    serializer_class = serializers.AddressSerializer
    queryset = Address.objects.order_by("-id")
