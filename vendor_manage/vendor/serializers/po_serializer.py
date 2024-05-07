from rest_framework import serializers
from vendor.configurations.basic_config import STATUS_CHOICES


class PoCreateSerializer(serializers.Serializer):
    vendor_id = serializers.IntegerField(
        required=True,
        help_text="Primary key of a vendor",
        error_messages={
            "required": "vendor id is required.",
            "invalid": "vendor id must be an integer.",
        },
    )
    items = serializers.JSONField(
        required=True,
        help_text="Purchased items",
        error_messages={
            "required": "Items is required.",
            "invalid": "Items must be an JSON.",
        },
    )
    quantity = serializers.IntegerField(
        required=True,
        help_text="quantity of a purchased items",
        error_messages={
            "required": "quantity is required.",
            "invalid": "quantity must be an int.",
        },
    )
    status = serializers.CharField(
        required=True,
        help_text="status of a purchased order",
        allow_blank=False,
        error_messages={
            "required": "status is required.",
            "invalid": "status must be an char.",
        },
    )
    quality_rating = serializers.FloatField(
        required=True,
        help_text="quality_rating of a items",
        error_messages={
            "required": "quality_rating is required.",
            "invalid": "quality_rating must be an Float.",
        },
    )

    def validate(self, attrs):
        for key, value in attrs.items():
            if isinstance(value, int) and value <= 0:
                raise serializers.ValidationError(
                    f"{key} value must be integer and greater than zero."
                )
            if isinstance(value, float) and value <= 0.0:
                raise serializers.ValidationError(
                    f"{key} value must be float and greater than zero."
                )
            if key == "status":
                if value not in ["PENDING", "COMPLETED", "CANCELED"]:
                    raise serializers.ValidationError(
                        f"{key} value must be PENDING, COMPLETED or CANCELED."
                    )
        return attrs


class PoUpdateSerializer(serializers.Serializer):
    status = serializers.CharField(
        required=True,
        help_text="status of a purchased order",
        allow_blank=False,
        error_messages={
            "required": "status is required.",
            "invalid": "status must be an char.",
        },
    )
    quality_rating = serializers.FloatField(
        required=True,
        help_text="quality_rating of a items",
        error_messages={
            "required": "quality_rating is required.",
            "invalid": "quality_rating must be an Float.",
        },
    )
    delivery_date = serializers.DateTimeField(
        required=True,
        help_text="delivery_date of a items",
        error_messages={
            "required": "delivery_date is required.",
            "invalid": "delivery_date must be an Float.",
        },
    )
    issue_date = serializers.DateTimeField(
        required=True,
        help_text="issue_date of a items",
        error_messages={
            "required": "issue_date is required.",
            "invalid": "issue_date must be an Float.",
        },
    )

    def validate(self, attrs):
        for key, value in attrs.items():
            if isinstance(value, int) and value <= 0:
                raise serializers.ValidationError(
                    f"{key} value must be integer and greater than zero."
                )
            if isinstance(value, float) and value <= 0.0:
                raise serializers.ValidationError(
                    f"{key} value must be float and greater than zero."
                )
            if key == "status":
                if value not in ["PENDING", "COMPLETED", "CANCELED"]:
                    raise serializers.ValidationError(
                        f"{key} value must be PENDING, COMPLETED or CANCELED."
                    )
        return attrs
