from django.urls import path

from .views import CustomerAPIView


app_name = "customer"


urlpatterns = [
    path("create_customer/", CustomerAPIView.as_view(), name="create-customer"),
]
