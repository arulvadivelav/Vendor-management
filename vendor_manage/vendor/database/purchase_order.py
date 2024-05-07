from vendor.models import PurchaseOrder


def po_create(data):
    return PurchaseOrder.objects.create(**data)


def get_specific_po(condition):
    return PurchaseOrder.objects.filter(**condition).last()


def get_all_po():
    return PurchaseOrder.objects.all().order_by("id")


def po_update(condition, data):
    return PurchaseOrder.objects.filter(**condition).update(**data)
