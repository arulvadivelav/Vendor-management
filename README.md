# Vendor Management System
## Description
The vendor management REST API service that includes vendor resigration. The vendors can add Purchase orders and acknowledge and update the status once the order has been delivered to the end user.

## Installation
### Clone the repository
$ https://github.com/arulvadivelav/Vendor-management.git

### Create a virtual environment
```python3 -m venv vendor_env```

### Activate virtual environment
```vendor_env/Scipts/activate.bat```

### Navigate to the project directory
```cd vendor_manage```

### Install dependencies
```pip install -r requirements.in```

Update the __settings.py__ file with the necessary configuration parameters.

udpate the database section of __vendor_manage/settings.py__ as per your local configuration

## Apply migrations
```python manage.py migrate```

## Run a application
```python manage.py runserver```

## The complete API doc can be found here
http://127.0.0.1:8000/api/schema/swagger-ui/

