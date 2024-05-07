from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from vendor.repository.vendor_create_repo import (
    get_vendor_performance,
    new_vendor_repo,
    get_vendor_detail,
    update_vendor_repo,
)
from vendor.serializers.vendor_serializer import vendorCreateSerializer
from vendor.database.ventor import get_all_vendors, get_specific_vendor
from drf_spectacular.utils import extend_schema


class VendorCreate(APIView):
    """This endpoint is used to get all Vendor details"""

    @extend_schema(
        tags=["Vendor"],
    )
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
            else:
                return Response(
                    {
                        "status": False,
                        "message": "Records not found.",
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
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

    @extend_schema(
        tags=["Vendor"],
        request=vendorCreateSerializer,
    )
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

    @extend_schema(
        tags=["Vendor"],
    )
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

    @extend_schema(
        tags=["Vendor"],
        request=vendorCreateSerializer,
    )
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

    """This endpoint is used to delete a specific Vendor details"""

    @extend_schema(
        tags=["Vendor"],
    )
    def delete(self, request, vendor_id):
        try:
            condition = {"id": vendor_id}
            vendor = get_specific_vendor(condition)
            if vendor:
                vendor.delete()
                return Response(
                    {
                        "status": True,
                        "data": {},
                        "message": "Vendor details deleted successfully.",
                        "statuscode": 200,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": False,
                        "message": "Vendor details not found.",
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print("Exception Occured while delete a specific vendor details:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class VendorPerformance(APIView):
    """This endpoint is used to get Vendor Performance details"""

    @extend_schema(
        tags=["Performance"],
    )
    def get(self, request, vendor_id):
        try:
            resStatus, vendorDetail, resMsg = get_vendor_performance(vendor_id)
            if resStatus:
                return Response(
                    {
                        "status": True,
                        "data": vendorDetail,
                        "message": "Vendor performance details provided successfully.",
                        "statuscode": 200,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "status": False,
                        "message": "Records not found.",
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print("Exception Occured in get vendor performance details:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
