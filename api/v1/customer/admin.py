from django.contrib import admin

# Register your models here.
from api.v1.customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    readonly_fields = (
        "uuid",
        "created",
        "modified",
    )
    search_fields = [
        "id",
        "first_name",
        "last_name",
    ]
    list_display = [
        "id",
        "first_name",
        "last_name",
        "dob",
        "is_active",
        "created",
    ]
    list_filter = [
        "is_active",
        "created",
        "modified",
    ]
