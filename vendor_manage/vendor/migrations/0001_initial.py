# Generated by Django 5.0.4 on 2024-05-07 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("contact_details", models.TextField()),
                ("address", models.TextField()),
                ("vendor_code", models.CharField(max_length=50, unique=True)),
                ("on_time_delivery_rate", models.FloatField()),
                ("quality_rating_avg", models.FloatField()),
                ("average_response_time", models.FloatField()),
                ("fulfillment_rate", models.FloatField()),
            ],
            options={
                "db_table": "vm_vendor",
            },
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("po_number", models.CharField(max_length=50, unique=True)),
                ("order_date", models.DateTimeField(auto_now=True, null=True)),
                ("delivery_date", models.DateTimeField(null=True)),
                ("items", models.JSONField(null=True)),
                ("quantity", models.IntegerField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "PENDING"),
                            ("COMPLETED", "COMPLETED"),
                            ("CANCELED", "CANCELED"),
                        ],
                        max_length=10,
                    ),
                ),
                ("quality_rating", models.FloatField(null=True)),
                ("issue_date", models.DateTimeField(null=True)),
                ("acknowledgment_date", models.DateTimeField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="vendor.vendor",
                    ),
                ),
            ],
            options={
                "db_table": "vm_purchase_order",
            },
        ),
        migrations.CreateModel(
            name="HistoricalPerformance",
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
                ("date", models.DateTimeField(null=True)),
                ("on_time_delivery_rate", models.FloatField(default=0, max_length=100)),
                ("quality_rating_avg", models.FloatField(default=0, max_length=100)),
                ("average_response_time", models.FloatField(default=0, max_length=100)),
                ("fulfillment_rate", models.FloatField(default=0, max_length=100)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="vendor.vendor",
                    ),
                ),
            ],
            options={
                "db_table": "vm_historical_performance",
            },
        ),
    ]
