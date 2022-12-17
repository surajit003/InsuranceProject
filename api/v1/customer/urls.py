from django.urls import path

from .views import CustomerAPIView


app_name = "customer"


urlpatterns = [
    path("customers/", CustomerAPIView.as_view(), name="customers"),
]
