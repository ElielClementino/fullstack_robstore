from robstore.accounts.models import User
from model_bakery import baker
from . import fixtures
import json


def test_deve_retornar_usuario_nao_logado(client):
    resp = client.get("/api/accounts/whoami")

    assert resp.status_code == 200
    assert resp.json() == {"authenticated": False}


def test_deve_retornar_usuario_logado(client, db):
    fixtures.user_jon()

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/accounts/whoami")

    data = resp.json()
    assert resp.status_code == 200
    assert data == {
        "user": {
            "id": 1,
            "name": "Jon Snow",
            "username": "jon",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jon@example.com",
            "permissions": {"ADMIN": False, "STAFF": False},
        },
        "authenticated": True,
    }


def test_deve_fazer_login(client, db):
    fixtures.user_jon()
    resp = client.post("/api/accounts/login", {"username": "jon", "password": "snow"})
    login = resp.json()

    resp = client.get("/api/accounts/whoami")
    data = resp.json()

    assert login["email"] == "jon@example.com"
    assert resp.status_code == 200
    assert data == {
        "user": {
            "id": 2,
            "name": "Jon Snow",
            "username": "jon",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jon@example.com",
            "permissions": {"ADMIN": False, "STAFF": False},
        },
        "authenticated": True,
    }


def test_deve_fazer_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/accounts/logout")

    assert resp.status_code == 200
    assert not resp.json()


def test_deve_fazer_logout_mesmo_sem_login(client, db):
    resp = client.post("/api/accounts/logout")
    assert resp.status_code == 200


def test_not_registering_if_equal_username(client, db):
    baker.make(User, username="Roberto", password="Roberto")

    new_user = {"userInfo": { "username": "Roberto", "email":"roberto@gmail.com", "password": "Roberto"}}

    response = client.post("/api/accounts/register", new_user, content_type="application/json")
    data = json.loads(response.content.decode())


    assert response.status_code == 200
    assert data == {'erro': 'nome de usuário já está sendo usado'}


def test_not_registering_if_equal_email(client, db):
    baker.make(User, username="Roberto", password="Roberto", email="roberto@gmail.com")

    new_user = {"userInfo": { "username": "Liel", "email":"roberto@gmail.com", "password": "Roberto"}}

    response = client.post("/api/accounts/register", new_user, content_type="application/json")
    data = json.loads(response.content.decode())


    assert response.status_code == 200
    assert data == {'erro': 'email já está sendo usado'}


def test_user_registering_is_working(client, db):
    new_user = {"userInfo": { "username": "Liel", "email":"roberto@gmail.com", "password": "Roberto"}}

    response = client.post("/api/accounts/register", new_user, content_type="application/json")
    data = json.loads(response.content.decode())

    assert response.status_code == 200
    assert data == {'sucesso': f'usuário { new_user["userInfo"]["username"] }, sua conta foi criada com sucesso '}
