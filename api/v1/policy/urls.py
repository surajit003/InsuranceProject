from django.urls import path

from .views import PolicyAPIView, PolicyRetrieveAPIView, PolicyListAPIView

app_name = "policy"


urlpatterns = [
    path("quote/", PolicyAPIView.as_view(), name="quote-create"),
    path("quotes/<uuid:uuid>/", PolicyRetrieveAPIView.as_view(), name="quote-detail"),
    path("quotes/", PolicyListAPIView.as_view(), name="quote-list"),
]
