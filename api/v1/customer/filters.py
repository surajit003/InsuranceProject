import django_filters

from .models import Customer


class CustomerFilterSet(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        field_name="first_name",
        lookup_expr="icontains",
    )
    last_name = django_filters.CharFilter(
        field_name="last_name",
        lookup_expr="icontains",
    )

    dob = django_filters.DateFilter(field_name="dob")

    class Meta:
        model = Customer
        fields = "first_name", "last_name", "dob"
