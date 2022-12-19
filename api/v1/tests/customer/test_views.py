import pytest
from mixer.backend.django import mixer

from api.v1.customer.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_create(client):
    response = client.post(
        "/api/v1/create_customer/",
        data={"first_name": "test", "last_name": "user", "dob": "21-03-1990"},
    )
    resp_json = response.json()
    assert response.status_code == 201
    assert resp_json["first_name"] == "test"
    assert resp_json["last_name"] == "user"
    assert resp_json["dob"] == "1990-03-21"


def test_customer_create_raises_validation_error_for_missing_first_name(client):
    response = client.post(
        "/api/v1/create_customer/", data={"last_name": "user", "dob": "21-03-1990"}
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["first_name"] == ["This field is required."]


def test_customer_create_raises_validation_error_for_incorrect_dob_format(client):
    response = client.post(
        "/api/v1/create_customer/",
        data={"first_name": "test", "last_name": "user", "dob": "03/21/1990"},
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["dob"] == [
        "Date has wrong format. Use one of these formats instead: DD-MM-YYYY."
    ]


def test_customer_get(client):
    customer = mixer.blend(Customer)
    response = client.get(
        f"/api/v1/customers/{customer.uuid}/",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json
    assert resp_json["first_name"] == customer.first_name
    assert resp_json["last_name"] == customer.last_name
    assert resp_json["dob"] == str(customer.dob)


def test_customers(client):
    mixer.blend(Customer)
    mixer.blend(Customer)
    response = client.get("/api/v1/customers/")
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json
    assert len(resp_json) == 2


def test_customers_search_by_first_name(client):
    customer_1 = mixer.blend(Customer, first_name="test")
    mixer.blend(Customer, first_name="user")
    response = client.get(f"/api/v1/customers/?first_name={customer_1.first_name}")
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json
    assert len(resp_json) == 1
    assert resp_json[0]["first_name"] == customer_1.first_name
    assert resp_json[0]["last_name"] == customer_1.last_name


def test_customers_search_by_last_name(client):
    mixer.blend(Customer, last_name="test")
    customer_2 = mixer.blend(Customer, last_name="user")
    response = client.get(f"/api/v1/customers/?last_name={customer_2.last_name}")
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json
    assert len(resp_json) == 1
    assert resp_json[0]["first_name"] == customer_2.first_name
    assert resp_json[0]["last_name"] == customer_2.last_name


def test_customers_search_by_dob(client):
    mixer.blend(Customer, dob="1990-03-21")
    customer_2 = mixer.blend(Customer, dob="1985-03-22")
    response = client.get(f"/api/v1/customers/?dob={customer_2.dob}")
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json
    assert len(resp_json) == 1

    assert resp_json[0]["first_name"] == customer_2.first_name
    assert resp_json[0]["last_name"] == customer_2.last_name
    assert resp_json[0]["dob"] == str(customer_2.dob)
