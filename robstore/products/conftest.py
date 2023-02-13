import pytest

from robstore.products.models import User


@pytest.fixture
def user(db):
    user = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
    )
    return user
