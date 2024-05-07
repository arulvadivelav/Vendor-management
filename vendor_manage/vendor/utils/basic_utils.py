from datetime import datetime, timedelta
import pytz

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
UTC_DATETIME = datetime.now(pytz.utc).strftime(DATETIME_FORMAT)

"""Function to check value is string or not"""


def is_string(input_value):
    return isinstance(input_value, str)


"""Function to get delivery datetime"""


def delivery_datetime(order_datetime, days_to_add):
    if isinstance(order_datetime, str):
        order_datetime = datetime.strptime(order_datetime, DATETIME_FORMAT)

    delivery_date = order_datetime + timedelta(days=days_to_add)
    return delivery_date.strftime(DATETIME_FORMAT)
