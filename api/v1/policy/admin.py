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
        "get_state",
    ]
    list_filter = [
        "state",
        "customer",
        "modified",
    ]

    def get_state(self, obj):
        return obj.get_state_display()

    get_state.short_description = "State"
