from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from model_mommy import mommy


class UserViewSetTestCase(APITestCase):
    """
    Test suite for User api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")

        self.post_data = {"username": "JamesJudy"}

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("api_users:user-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_user_post(self):
        """
        Test User creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.json()["username"], "JamesJudy")
        self.assertEqual(self.response.json()["first_name"], "")

    def test_anonymous_user_user_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        User.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("api_users:user-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_user_list(self):
        """
        Test the api endpoint for list user.
        """
        response = self.client.get(
            reverse("api_users:user-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_user_list(self):
        """
        Test the api endpoint for list user using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:user-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json["count"], 0)

    def test_get_user_retrieve(self):
        """
        Test the api endpoint for retrieve User.
        """
        response = self.client.get(
            reverse(
                "api_users:user-detail",
                args=[self.api_version, self.new_user.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_user_retrieve(self):
        """
        Test the api endpoint for retrieve User using request from
        anonymous user.
        """
        new_client = APIClient()
        new_user = mommy.make("users.User")
        new_response = new_client.get(
            reverse(
                "api_users:user-detail", args=[self.api_version, new_user.id]
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_404_NOT_FOUND)


class AddressViewSetTestCase(APITestCase):
    """
    Test suite for Address api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")

        self.post_data = {
            "address1": "Test Address",
            "city": "Test City",
            "country": "Kenya",
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("api_users:addresses-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_address_post(self):
        """
        Test Address creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.json()["address1"], "Test Address")
        self.assertEqual(self.response.json()["city"], "Test City")
        self.assertEqual(self.response.json()["country"], "Kenya")
        self.assertEqual(self.response.json()["county"], "")

    def test_anonymous_user_address_post(self):
        """
        Test if the api can raise error if anonymous user tries to create an
        Address.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("api_users:addresses-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_addresses_list(self):
        """
        Test the api endpoint for list addresses.
        """
        response = self.client.get(
            reverse("api_users:addresses-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_addresses_list(self):
        """
        Test the api endpoint for list addresses using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:addresses-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json["count"] > 0, True)

    def test_retrieve_address(self):
        """
        Test the api endpoint for retrieve Address.
        """
        response = self.client.get(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.new_user.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_retrieve_address(self):
        """
        Test the api endpoint for retrieve Address using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:addresses-detail", args=[self.api_version, 1])
        )
        self.assertEqual(new_response.status_code, status.HTTP_404_NOT_FOUND)
