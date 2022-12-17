from django.contrib import admin

# Register your models here.
from api.v1.policy.models import Policy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    model = Policy
    readonly_fields = (
        "uuid",
        "created",
        "modified",
        "state",
    )
    search_fields = [
        "id",
        "type",
        "customer",
    ]
    list_display = [
        "id",
        "type",
        "cover",
        "customer",
        "state",
    ]
    list_filter = [
        "state",
        "customer",
        "modified",
    ]
