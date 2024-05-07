from vendor.models import HistoricalPerformance


def get_specific_vendor_performance(condition):
    return HistoricalPerformance.objects.filter(**condition).last()
