from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from vendor.repository.vendor_create_repo import (
    new_vendor_repo,
    get_vendor_detail,
    update_vendor_repo,
)
from vendor.serializers.vendor_serializer import vendorCreateSerializer
from vendor.database.ventor import get_all_vendors


class VendorCreate(APIView):
    """This endpoint is used to get all Vendor details"""

    def get(self, request):
        try:
            vendor_details = get_all_vendors()
            if vendor_details:
                vendor_details_list = []
                for vendor in vendor_details:
                    resStatus, vendorDetail, resMsg = get_vendor_detail(vendor.id)
                    vendor_details_list.append(vendorDetail)
                return Response(
                    {
                        "status": True,
                        "data": vendor_details_list,
                        "message": "Vendor details provided successfully.",
                        "statuscode": 200,
                    },
                    status=status.HTTP_201_CREATED,
                )

        except Exception as e:
            print("Exception Occured in get vendor details list:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    """This endpoint is used to create a Vendor details"""

    def post(self, request):
        try:
            serializer = vendorCreateSerializer(data=request.data)
            if serializer.is_valid():
                new_vendor = new_vendor_repo(request.data)
                if new_vendor:
                    return Response(
                        {
                            "status": True,
                            "message": "New vendor details created successfully.",
                            "statuscode": 200,
                        },
                        status=status.HTTP_201_CREATED,
                    )
            else:
                return Response(
                    {
                        "status": False,
                        "message": str(serializer.errors),
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print("Exception Occured while create a vendor:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UpdateVendor(APIView):
    """This endpoint is used to get a specific Vendor details"""

    def get(self, request, vendor_id):
        try:
            reqStatus, vendor_details, resMsg = get_vendor_detail(vendor_id)
            if reqStatus:
                return Response(
                    {
                        "status": True,
                        "data": vendor_details,
                        "message": resMsg,
                        "statuscode": 200,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": False,
                        "message": resMsg,
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print("Exception Occured while get a specific vendor details:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    """This endpoint is used to update a specific Vendor details"""

    def put(self, request, vendor_id):
        try:
            serializer = vendorCreateSerializer(data=request.data)
            if serializer.is_valid():
                resStatus, updated_record, resMsg = update_vendor_repo(
                    request.data, vendor_id
                )
                if resStatus:
                    return Response(
                        {
                            "status": True,
                            "message": resMsg,
                            "statuscode": 200,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "status": False,
                            "message": resMsg,
                            "statuscode": 400,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        "status": False,
                        "message": str(serializer.errors),
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print("Exception Occured while update a specific vendor details:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
