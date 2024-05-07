vendor Management System
Description
The vendor management REST API service that includes vendor resigration into the system and authenticate them using Token based authentication. The vendors can add Purchase orders and acknowledge and update the status once the order has been delivered to the end user.

Table of Contents
Installation
Usage
Configuration
Installation
# Clone the repository
$ git clone https://github.com/SivaMadhavan/vms_vault.git

# Navigate to the project directory
$ cd vms_vault

create a virtual environment(unix)
$ python3 -m venv vms_env

# Install dependencies
$ pip install -r requirements.txt
Update the settings.py file with the necessary configuration parameters.

udpate the database section of vms_vault/settings.py as per your local configuration

Apply migrations
create a database named vms (if you are using mysql backend, ingore if you are using default sqlite3)

python manage.py migrate
Usage
# Run the development server
python manage.py runserver
The complete API doc can be found here http://localhost:8000/doc/

