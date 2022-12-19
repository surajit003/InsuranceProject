from django.urls import path

from .views import PolicyCreateAPIView, PolicyRetrieveUpdateAPIView, PolicyListAPIView

app_name = "policy"


urlpatterns = [
    path("quote/", PolicyCreateAPIView.as_view(), name="create-quote"),
    path(
        "quotes/<uuid:uuid>/",
        PolicyRetrieveUpdateAPIView.as_view(),
        name="quote",
    ),
    path("quotes/", PolicyListAPIView.as_view(), name="quotes"),
]
