from vendor.models import Vendor


def vendor_create(data):
    return Vendor.objects.create(**data)


def get_specific_vendor(condition):
    return Vendor.objects.filter(**condition).last()


def get_all_vendors():
    return Vendor.objects.all().order_by("id")


def vendor_update(condition, data):
    return Vendor.objects.filter(**condition).update(**data)
