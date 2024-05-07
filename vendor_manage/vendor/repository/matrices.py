from vendor.models import PurchaseOrder, HistoricalPerformance, Vendor
from datetime import timedelta
from django.db.models import F, Avg


def update_metrics_repo(instance):
    if instance.vendor:

        v_perf, created = HistoricalPerformance.objects.get_or_create(
            vendor=instance.vendor
        )
        vendor_ref = Vendor.objects.get(id=instance.vendor_id)
        po_qs = PurchaseOrder.objects.filter(vendor=instance.vendor)
        if instance.status == "COMPLETED":
            try:
                total = po_qs.count()

                # Find fulfilment rate
                completed = po_qs.filter(status="COMPLETED").count()
                v_perf.fulfillment_rate = round((completed / total) * 100, 2)
                vendor_ref.fulfillment_rate = round((completed / total) * 100, 2)

                # Find on time delivery rate
                before_del_date = po_qs.filter(
                    issue_date__lte=F("delivery_date")
                ).count()
                v_perf.on_time_delivery_rate = round(
                    (before_del_date / completed) * 100, 2
                )
                vendor_ref.on_time_delivery_rate = round(
                    (before_del_date / completed) * 100, 2
                )

                # Find average response time
                average = po_qs.annotate(
                    diff=F("issue_date") - F("acknowledgment_date")
                ).aggregate(avg=Avg("diff"))
                if average and isinstance(average.get("avg"), timedelta):
                    average = average.get("avg")
                    v_perf.average_response_time = average.total_seconds()
                    vendor_ref.average_response_time = average.total_seconds()
            except ZeroDivisionError as e:
                pass

        if instance.quality_rating:
            rating = po_qs.aggregate(average=Avg("quality_rating"))
            if rating.get("average"):
                v_perf.quality_rating_avg = rating.get("average")
                vendor_ref.quality_rating_avg = rating.get("average")

        v_perf.save()
        vendor_ref.save()
