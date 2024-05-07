from django.urls import path
from vendor.controller.vendor import VendorCreate, UpdateVendor, VendorPerformance
from vendor.controller.purchase_order import (
    PurchaseOrderCreate,
    UpdatePurchaseOrder,
    UpdatePoAcknowledge,
)

urlpatterns = [
    # Vendor CRUD
    path("vendors", VendorCreate.as_view()),
    path("vendors/<int:vendor_id>", UpdateVendor.as_view()),
    # Purchase Order CRUD
    path("purchase_orders", PurchaseOrderCreate.as_view()),
    path("purchase_orders/<int:po_id>", UpdatePurchaseOrder.as_view()),
    # Performance Details
    path("vendors/<int:vendor_id>/performance", VendorPerformance.as_view()),
    # Acknowledgment
    path("purchase_orders/<int:po_id>/acknowledge", UpdatePoAcknowledge.as_view()),
]
