# Generated by Django 4.1.4 on 2022-12-17 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customer", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Policy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("modified", models.DateTimeField(auto_now=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("type", models.CharField(max_length=120, verbose_name="Policy Type")),
                ("premium", models.IntegerField(verbose_name="Premium Amount")),
                ("cover", models.IntegerField(verbose_name="Cover")),
                (
                    "state",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "New"), (1, "Accepted"), (2, "Active")],
                        db_index=True,
                        default=0,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Policies",
            },
        ),
        migrations.CreateModel(
            name="HistoricalPolicy",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("modified", models.DateTimeField(blank=True, editable=False)),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4)),
                ("type", models.CharField(max_length=120, verbose_name="Policy Type")),
                ("premium", models.IntegerField(verbose_name="Premium Amount")),
                ("cover", models.IntegerField(verbose_name="Cover")),
                (
                    "state",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "New"), (1, "Accepted"), (2, "Active")],
                        db_index=True,
                        default=0,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="customer.customer",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical policy",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
