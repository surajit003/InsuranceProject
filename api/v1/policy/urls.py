from django.urls import path

from .views import QuoteAPIView


app_name = "policy"


urlpatterns = [
    path("quote/", QuoteAPIView.as_view(), name="quote"),
]
