import pytest
from mixer.backend.django import mixer

from api.v1.customer.models import Customer
from api.v1.policy.models import Policy

pytestmark = pytest.mark.django_db


def test_quote_create(client):
    customer = mixer.blend(Customer, dob="1990-03-21")
    response = client.post(
        "/api/v1/quote/",
        data={"customer_id": customer.id, "type": "personal-health"},
    )
    resp_json = response.json()
    assert response.status_code == 201
    assert resp_json["type"] == "personal-health"
    assert resp_json["customer_id"] == customer.id


def test_quote_create_raises_validation_error(client):
    response = client.post(
        "/api/v1/quote/",
        data={},
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["type"] == ["This field is required."]
    assert resp_json["customer_id"] == ["This field is required."]


def test_get_quote(client):
    customer = mixer.blend(Customer, dob="1990-03-21")
    policy = mixer.blend(Policy, customer=customer)
    response = client.get(
        f"/api/v1/quotes/{policy.uuid}/",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json["cover"] == 2000000
    assert resp_json["premium"] == 83333
    assert resp_json["customer"]


def test_search_policies_by_customer_id(client):
    customer = mixer.blend(Customer)
    mixer.blend(Policy, customer=customer)
    mixer.blend(Policy, customer=customer)
    response = client.get(
        f"/api/v1/quotes/?customer_id={customer.id}",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json) == 2


def test_search_policies_by_policy_type(client):
    policy_1 = mixer.blend(Policy, type="health benefit")
    mixer.blend(Policy, type="accident")
    response = client.get(
        f"/api/v1/quotes/?type={policy_1.type}",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json) == 1
    assert resp_json[0]["type"] == policy_1.type


def test_update_quote_status_as_accepted(client):
    policy = mixer.blend(Policy)
    assert policy.state == "new"
    response = client.patch(
        f"/api/v1/quotes/{policy.uuid}/",
        data={"state": "accepted"},
        content_type="application/json",
    )
    assert response.status_code == 200
    # lets check if the state was now marked as paid simulating the payment flow in signals
    policy = Policy.objects.filter(id=policy.id).first()
    assert policy.state == "active"


def test_update_quote_status_from_new_to_active(client):
    policy = mixer.blend(Policy, state="new")
    assert policy.state == "new"
    response = client.patch(
        f"/api/v1/quotes/{policy.uuid}/",
        data={"state": "active"},
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["non_field_errors"] == [
        "Cannot transition policy state from new to active"
    ]


def test_update_quote_status_from_active_to_new(client):
    policy = mixer.blend(Policy, state="active")
    assert policy.state == "active"
    response = client.patch(
        f"/api/v1/quotes/{policy.uuid}/",
        data={"state": "new"},
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["non_field_errors"] == [
        "Cannot transition policy state from active to new"
    ]
