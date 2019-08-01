from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from model_mommy import mommy


class UserViewSetTestCaseV1(APITestCase):
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

    def test_user_post_v1(self):
        """
        Test User creation.
        """

        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.json()["username"], "JamesJudy")
        self.assertEqual(self.response.json()["first_name"], "")

    def test_anonymous_user_user_post_v1(self):
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

    def test_get_user_list_v1(self):
        """
        Test the api endpoint for list user.
        """

        response = self.client.get(
            reverse("api_users:user-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_user_list_v1(self):
        """
        Test the api endpoint for list user using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:user-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json()["count"], 0)

    def test_get_user_retrieve_v1(self):
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

    def test_anonymous_user_get_user_retrieve_v1(self):
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


class UserViewSetTestCaseV2(APITestCase):
    """
    Test suite for User api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v2"
        self.new_user = mommy.make("users.User")

        self.post_data = {"username": "JamesJudy"}

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("api_users:user-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_user_post_v2(self):
        """
        Test User creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.json()["username"], "JamesJudy")
        self.assertEqual(self.response.json()["first_name"], "")

    def test_anonymous_user_user_post_v2(self):
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

    def test_get_user_list_v2(self):
        """
        Test the api endpoint for list user.
        """

        response = self.client.get(
            reverse("api_users:user-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_user_list_v2(self):
        """
        Test the api endpoint for list user using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:user-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json()["count"], 0)

    def test_get_user_retrieve_v2(self):
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

    def test_anonymous_user_get_user_retrieve_v2(self):
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


class AddressViewSetTestCaseV1(APITestCase):
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
            "postcode": "00503",
            "country": "KE",
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("api_users:addresses-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_address_post_v1(self):
        """
        Test Address creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.json()["address1"], "Test Address")
        self.assertEqual(self.response.json()["city"], "Test City")
        self.assertEqual(self.response.json()["country"], "KE")
        self.assertEqual(self.response.json()["county"], "")

    def test_anonymous_user_address_post_v1(self):
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

    def test_get_addresses_list_v1(self):
        """
        Test the api endpoint for list addresses.
        """

        response = self.client.get(
            reverse("api_users:addresses-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_addresses_list_v1(self):
        """
        Test the api endpoint for list addresses using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:addresses-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json()["count"] > 0, True)

    def test_retrieve_address_v1(self):
        """
        Test the api endpoint for retrieve Address.
        """

        response = self.client.get(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_retrieve_address_v1(self):
        """
        Test the api endpoint for retrieve Address using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_address_put_v1(self):
        """
        Test address update through PUT request.
        """

        post_data = {
            "address1": "Test Address 1",
            "city": "Test City 1",
            "postcode": "00503",
            "country": "KE",
        }
        response = self.client.put(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["address1"], "Test Address 1")
        self.assertEqual(response.json()["city"], "Test City 1")
        self.assertEqual(response.json()["postcode"], "00503")
        self.assertEqual(response.json()["country"], "KE")

    def test_anonymous_user_address_put_v1(self):
        """
        Test if the api can raise error if anonymous user tries to PUT an
        Address.
        """

        new_client = APIClient()
        post_data = {
            "address1": "Test Address 2",
            "city": "Test City 2",
            "postcode": "00503",
            "country": "KE",
        }
        new_response = new_client.put(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
        self.assertEqual(
            new_response.json()["detail"],
            "Authentication credentials were not provided.",
        )

    def test_address_patch_v1(self):
        """
        Test address update through PATCH request.
        """

        post_data = {"address1": "Test Address 3", "city": "Test City 3"}
        response = self.client.patch(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["address1"], "Test Address 3")
        self.assertEqual(response.json()["city"], "Test City 3")

    def test_anonymous_user_address_patch_v1(self):
        """
        Test if the api can raise error if anonymous user tries to PUT an
        Address.
        """

        new_client = APIClient()
        post_data = {"address1": "Test Address 4", "city": "Test City 4"}
        new_response = new_client.patch(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
        self.assertEqual(
            new_response.json()["detail"],
            "Authentication credentials were not provided.",
        )


class AddressViewSetTestCaseV2(APITestCase):
    """
    Test suite for Address api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v2"
        self.new_user = mommy.make("users.User")

        self.post_data = {
            "address1": "Test Address",
            "city": "Test City",
            "postcode": "00503",
            "country": "KE",
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("api_users:addresses-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_address_post_v2(self):
        """
        Test Address creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.json()["address1"], "Test Address")
        self.assertEqual(self.response.json()["city"], "Test City")
        self.assertEqual(self.response.json()["country"], "KE")
        self.assertEqual(self.response.json()["county"], "")

    def test_anonymous_user_address_post_v2(self):
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

    def test_get_addresses_list_v2(self):
        """
        Test the api endpoint for list addresses.
        """

        response = self.client.get(
            reverse("api_users:addresses-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_addresses_list_v2(self):
        """
        Test the api endpoint for list addresses using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:addresses-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json()["count"] > 0, True)

    def test_retrieve_address_v2(self):
        """
        Test the api endpoint for retrieve Address.
        """

        response = self.client.get(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_retrieve_address_v2(self):
        """
        Test the api endpoint for retrieve Address using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_address_put_v2(self):
        """
        Test address update through PUT request.
        """

        post_data = {
            "address1": "Test Address 1",
            "city": "Test City 1",
            "postcode": "00503",
            "country": "KE",
        }
        response = self.client.put(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["address1"], "Test Address 1")
        self.assertEqual(response.json()["city"], "Test City 1")
        self.assertEqual(response.json()["postcode"], "00503")
        self.assertEqual(response.json()["country"], "KE")

    def test_anonymous_user_address_put_v2(self):
        """
        Test if the api can raise error if anonymous user tries to PUT an
        Address.
        """

        new_client = APIClient()
        post_data = {
            "address1": "Test Address 2",
            "city": "Test City 2",
            "postcode": "00503",
            "country": "KE",
        }
        new_response = new_client.put(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
        self.assertEqual(
            new_response.json()["detail"],
            "Authentication credentials were not provided.",
        )

    def test_address_patch_v2(self):
        """
        Test address update through PATCH request.
        """

        post_data = {"address1": "Test Address 3", "city": "Test City 3"}
        response = self.client.patch(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["address1"], "Test Address 3")
        self.assertEqual(response.json()["city"], "Test City 3")

    def test_anonymous_user_address_patch_v2(self):
        """
        Test if the api can raise error if anonymous user tries to PUT an
        Address.
        """

        new_client = APIClient()
        post_data = {"address1": "Test Address 4", "city": "Test City 4"}
        new_response = new_client.patch(
            reverse(
                "api_users:addresses-detail",
                args=[self.api_version, self.response.json()["id"]],
            ),
            post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
        self.assertEqual(
            new_response.json()["detail"],
            "Authentication credentials were not provided.",
        )


class ProfileViewSetTestCaseV1(APITestCase):
    """
    Test suite for Prifile api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.get(
            reverse("api_users:profiles-list", args=[self.api_version])
        )

    def test_get_profiles_list_v1(self):
        """
        Test the api endpoint for list profiles.
        """

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.json()["count"] > 0, True)
        self.assertEqual(
            self.new_user.username
            in [
                profile["username"]
                for profile in self.response.json()["results"]
            ],
            True,
        )

    def test_anonymous_user_get_profiles_list_v1(self):
        """
        Test the api endpoint for list profiles using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:profiles-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json()["count"] > 0, True)
        self.assertEqual(
            self.new_user.username
            in [
                profile["username"]
                for profile in new_response.json()["results"]
            ],
            True,
        )

    def test_retrieve_profile_v1(self):
        """
        Test the api endpoint for retrieve Profile.
        """

        response = self.client.get(
            reverse(
                "api_users:profiles-detail",
                args=[self.api_version, self.new_user.username],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["username"], self.new_user.username)

    def test_anonymous_user_retrieve_profile_v1(self):
        """
        Test the api endpoint for retrieve Profile using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse(
                "api_users:profiles-detail",
                args=[self.api_version, self.new_user.username],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            new_response.json()["username"], self.new_user.username
        )


class ProfileViewSetTestCaseV2(APITestCase):
    """
    Test suite for Prifile api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v2"
        self.new_user = mommy.make("users.User")

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.get(
            reverse("api_users:profiles-list", args=[self.api_version])
        )

    def test_get_profiles_list_v2(self):
        """
        Test the api endpoint for list profiles.
        """

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.json()["count"] > 0, True)
        self.assertEqual(
            self.new_user.username
            in [
                profile["username"]
                for profile in self.response.json()["results"]
            ],
            True,
        )

    def test_anonymous_user_get_profiles_list_v2(self):
        """
        Test the api endpoint for list profiles using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse("api_users:profiles-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.json()["count"] > 0, True)
        self.assertEqual(
            self.new_user.username
            in [
                profile["username"]
                for profile in new_response.json()["results"]
            ],
            True,
        )

    def test_retrieve_profile_v2(self):
        """
        Test the api endpoint for retrieve Profile.
        """

        response = self.client.get(
            reverse(
                "api_users:profiles-detail",
                args=[self.api_version, self.new_user.username],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["username"], self.new_user.username)

    def test_anonymous_user_retrieve_profile_v2(self):
        """
        Test the api endpoint for retrieve Profile using request from
        anonymous user.
        """

        new_client = APIClient()
        new_response = new_client.get(
            reverse(
                "api_users:profiles-detail",
                args=[self.api_version, self.new_user.username],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            new_response.json()["username"], self.new_user.username
        )
