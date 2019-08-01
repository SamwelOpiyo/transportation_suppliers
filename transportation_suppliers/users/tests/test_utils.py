import pytest

from model_mommy import mommy

from transportation_suppliers.users.utils import (
    get_extension,
    user_avatar_path,
)


pytestmark = pytest.mark.django_db


def test_get_extension():
    """
    Test get_extension function.
    """

    assert get_extension("/home/user/profile_picture.jpeg") == ".jpeg"


def test_get_extension():
    """
    Test user_avatar_path function.
    """

    new_user = mommy.make("users.User")
    avatar_path = user_avatar_path(new_user, "/home/user/profile_picture.jpeg")
    assert avatar_path.split("/")[0] == "avatars"
    assert avatar_path.split("/")[1] == new_user.username
    assert avatar_path.split("/")[2][-5:] == ".jpeg"
