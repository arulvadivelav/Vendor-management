from vendor.database.ventor import get_specific_vendor, vendor_create, vendor_update


def new_vendor_repo(data):
    """Repo function to create a new vendor"""

    name = data["name"]
    contact_details = data["contact_details"]
    address = data["address"]
    data = {"name": name, "contact_details": contact_details, "address": address}
    return vendor_create(data)


def get_vendor_detail(vendor_id):
    """Repo function to get a specific vendor details"""
    condition = {"id": vendor_id}
    vendor = get_specific_vendor(condition)
    if vendor:
        data = {
            "id": vendor.id,
            "name": vendor.name,
            "contact_details": vendor.contact_details,
            "address": vendor.address,
            "vendor_code": vendor.vendor_code,
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate,
        }
        return True, data, "Vendor details provided successfully."
    else:
        return False, {}, "Vendor details not found."


def update_vendor_repo(data, vendor_id):
    """Repo function to update a existing vendor details"""
    condition = {"id": vendor_id}
    vendor = get_specific_vendor(condition)
    if vendor:
        name = data["name"]
        contact_details = data["contact_details"]
        address = data["address"]
        data = {"name": name, "contact_details": contact_details, "address": address}
        update_vendor_details = vendor_update(condition, data)
        return True, {}, "Vendor details updated successfully."
    else:
        return False, {}, "Vendor details not found."
