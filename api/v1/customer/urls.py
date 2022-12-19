from django.urls import path

from .views import CustomerCreateAPIView, CustomerListAPIView, CustomerRetrieveAPIView

app_name = "customer"


urlpatterns = [
    path("create_customer/", CustomerCreateAPIView.as_view(), name="create-customer"),
    path("customers/<uuid:uuid>/", CustomerRetrieveAPIView.as_view(), name="customer"),
    path("customers/", CustomerListAPIView.as_view(), name="customers"),
]
