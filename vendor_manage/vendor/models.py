from django.db import models
from uuid import uuid4
from vendor.configurations.basic_config import STATUS_CHOICES


class Vendor(models.Model):
    class Meta:
        db_table = "vm_vendor"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_details = models.TextField(null=True)
    address = models.TextField(null=True)
    vendor_code = models.CharField(max_length=50, unique=True, default=uuid4)
    on_time_delivery_rate = models.FloatField(default=0, null=True)
    quality_rating_avg = models.FloatField(default=0, null=True)
    average_response_time = models.FloatField(default=0, null=True)
    fulfillment_rate = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.id


class PurchaseOrder(models.Model):
    class Meta:
        db_table = "vm_purchase_order"

    id = models.AutoField(primary_key=True)
    po_number = models.CharField(max_length=50, unique=True, default=uuid4)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING, null=False)
    order_date = models.DateTimeField(auto_now=True, null=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField(null=True)
    quantity = models.IntegerField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(null=True)
    acknowledgment_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HistoricalPerformance(models.Model):
    class Meta:
        db_table = "vm_historical_performance"

    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(null=True)
    on_time_delivery_rate = models.FloatField(default=0, max_length=100)
    quality_rating_avg = models.FloatField(default=0, max_length=100)
    average_response_time = models.FloatField(default=0, max_length=100)
    fulfillment_rate = models.FloatField(default=0, max_length=100)
