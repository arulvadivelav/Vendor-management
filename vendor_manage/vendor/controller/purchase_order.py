from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from vendor.database.purchase_order import get_all_po, get_specific_po
from vendor.models import PurchaseOrder
from vendor.repository.purchase_order_repo import (
    get_po_detail,
    new_po_repo,
    update_po_repo,
)
from vendor.serializers.po_serializer import PoCreateSerializer, PoUpdateSerializer
from vendor.utils.basic_utils import UTC_DATETIME
from drf_spectacular.utils import extend_schema


class PurchaseOrderCreate(APIView):
    """This endpoint is used to get all purchase order details"""

    @extend_schema(
        tags=["Purchase Order"],
    )
    def get(self, request):
        try:
            po_details = get_all_po()
            if po_details:
                po_details_list = []
                for po in po_details:
                    resStatus, PoDetail, resMsg = get_po_detail(po.id)
                    po_details_list.append(PoDetail)
                return Response(
                    {
                        "status": True,
                        "data": po_details_list,
                        "message": "Purchase order details provided successfully.",
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
            print("Exception Occured in get urchase order list:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    """This endpoint is used to create a purchase order details"""

    @extend_schema(
        tags=["Purchase Order"],
        request=PoCreateSerializer,
    )
    def post(self, request):
        try:
            serializer = PoCreateSerializer(data=request.data)
            if serializer.is_valid():
                res_status, new_po, res_msg = new_po_repo(request.data)
                if res_status:
                    return Response(
                        {
                            "status": True,
                            "message": res_msg,
                            "statuscode": 200,
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {
                            "status": False,
                            "message": res_msg,
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
            print("Exception Occured while create a purchase order:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UpdatePurchaseOrder(APIView):
    """This endpoint is used to get a specific purchase order details"""

    @extend_schema(
        tags=["Purchase Order"],
    )
    def get(self, request, po_id):
        try:
            reqStatus, po_details, resMsg = get_po_detail(po_id)
            if reqStatus:
                return Response(
                    {
                        "status": True,
                        "data": po_details,
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
            print("Exception Occured while get a specific purchase order details:", e)
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    """This endpoint is used to update a specific purchase order details"""

    @extend_schema(
        tags=["Purchase Order"],
        request=PoUpdateSerializer,
    )
    def put(self, request, po_id):
        try:
            serializer = PoUpdateSerializer(data=request.data)
            if serializer.is_valid():
                resStatus, updated_record, resMsg = update_po_repo(request.data, po_id)
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
            print(
                "Exception Occured while update a specific purchase order details:", e
            )
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    """This endpoint is used to delete a specific purchase order details"""

    @extend_schema(
        tags=["Purchase Order"],
    )
    def delete(self, request, po_id):
        try:
            condition = {"po_number": po_id}
            po = get_specific_po(condition)
            if po:
                po.delete()
                return Response(
                    {
                        "status": True,
                        "data": {},
                        "message": "Purchase order details deleted successfully.",
                        "statuscode": 200,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": False,
                        "message": "Purchase order details not found.",
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print(
                "Exception Occured while delete a specific purchase order details:", e
            )
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UpdatePoAcknowledge(APIView):
    """This endpoint is used to update a specific purchase order acknowledgment date"""

    @extend_schema(
        tags=["Acknowledgement"],
    )
    def put(self, request, po_id):
        try:
            po = PurchaseOrder.objects.get(id=po_id)
            if po:
                po.acknowledgment_date = UTC_DATETIME
                po.save()
                return Response(
                    {
                        "status": True,
                        "message": "Order acknowledged successfully.",
                        "statuscode": 200,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": False,
                        "message": "Purchase order not found",
                        "statuscode": 400,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print(
                "Exception Occured while update a specific purchase order acknowledge date:",
                e,
            )
            return Response(
                {
                    "status": False,
                    "message": "Process failed. Please try later.",
                    "statuscode": 500,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
