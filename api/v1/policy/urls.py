from django.urls import path

from .views import PolicyAPIView


app_name = "customer"


urlpatterns = [
    path("quote/", PolicyAPIView.as_view(), name="policy"),
]
