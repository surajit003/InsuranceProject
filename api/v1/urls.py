from django.urls import path
from django.conf.urls import include

app_name = "v1"

urlpatterns = [
    path("", include("api.v1.customer.urls")),
    path("", include("api.v1.policy.urls")),
]
