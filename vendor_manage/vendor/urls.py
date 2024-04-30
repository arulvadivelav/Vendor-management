from django.urls import path
from vendor.controller.vendor import VendorCreate, UpdateVendor

urlpatterns = [
    # Vendor CRUD
    path("vendors", VendorCreate.as_view()),
    path("vendors/<int:vendor_id>", UpdateVendor.as_view()),
]
