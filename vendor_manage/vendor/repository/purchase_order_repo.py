from vendor.database.purchase_order import get_specific_po, po_create, po_update
from datetime import timedelta
from vendor.database.ventor import get_specific_vendor
from vendor.models import PurchaseOrder
from vendor.utils.basic_utils import UTC_DATETIME, delivery_datetime


def new_po_repo(data):
    """Repo function to create a new purchase order"""

    vendor = data["vendor_id"]
    order_date = UTC_DATETIME
    delivery_date = delivery_datetime(order_date, 7)
    items = data["items"]
    quantity = data["quantity"]
    status = data["status"]
    quality_rating = data["quality_rating"]
    issue_date = delivery_datetime(order_date, 7)

    vendor_details = get_specific_vendor({"id": vendor})
    if not vendor_details:
        return False, {}, "Vendor details not found."
    data = {
        "vendor_id": vendor,
        "order_date": order_date,
        "delivery_date": delivery_date,
        "items": items,
        "quantity": quantity,
        "status": status,
        "quality_rating": quality_rating,
        "issue_date": issue_date,
    }
    return True, po_create(data), "Purchase order created successfully."


def get_po_detail(po_id):
    """Repo function to get a specific purchase order details"""
    condition = {"id": po_id}
    po = get_specific_po(condition)
    if po:
        data = {
            "po_number": po.po_number,
            "vendor_details": {
                "id": po.id,
                "name": po.vendor.name if po.vendor else None,
                "contact_details": po.vendor.contact_details if po.vendor else None,
                "address": po.vendor.address if po.vendor else None,
                "vendor_code": po.vendor.vendor_code if po.vendor else None,
            },
            "order_date": po.order_date,
            "delivery_date": po.delivery_date,
            "items": po.items,
            "quantity": po.quantity,
            "status": po.status,
            "quality_rating": po.quality_rating,
            "issue_date": po.issue_date,
            "acknowledgment_date": po.acknowledgment_date,
            "updated_at": po.updated_at,
        }
        return True, data, "Purchase order details provided successfully."
    else:
        return False, {}, "Purchase order details not found."


def update_po_repo(data, po_id):
    """Repo function to update a existing purchase order details"""
    condition = {"id": po_id}
    po = PurchaseOrder.objects.get(id=po_id)
    if po:
        po.delivery_date = data["delivery_date"]
        po.status = data["status"]
        po.quality_rating = data["quality_rating"]
        po.issue_date = data["issue_date"]
        po.save()

        return True, {}, "Purchase order details updated successfully."
    else:
        return False, {}, "Purchase order details not found."
