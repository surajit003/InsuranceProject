import django_filters

from .models import Policy


class PolicyFilterSet(django_filters.FilterSet):
    type = django_filters.CharFilter(
        field_name="type",
        lookup_expr="icontains",
    )
    customer_id = django_filters.CharFilter(field_name="customer__id")
    state = django_filters.CharFilter(field_name="state", lookup_expr="icontains")

    class Meta:
        model = Policy
        fields = "type", "customer_id", "state"
