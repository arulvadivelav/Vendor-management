from rest_framework import serializers


class vendorCreateSerializer(serializers.Serializer):
    name = serializers.CharField(
        help_text="Name of a vendor",
        allow_blank=False,
        error_messages={
            "required": "name is required.",
            "invalid": "name must be an char.",
        },
    )
    contact_details = serializers.CharField(
        help_text="Contact details of a vendor",
        allow_blank=False,
        error_messages={
            "required": "Contact details is required.",
            "invalid": "Contact details must be an char.",
        },
    )
    address = serializers.CharField(
        help_text="address of a vendor",
        allow_blank=False,
        error_messages={
            "required": "Address is required.",
            "invalid": "Address must be an char.",
        },
    )
