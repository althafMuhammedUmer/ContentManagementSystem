# ContentManagementSystem
This is a Django-based Content Management System (CMS) project that allows users to create, view, update, and delete content items along with various features like categorization and document attachment.

Table of Contents
Installation
Usage
Test Coverage
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/content-management-system.git
cd content-management-system
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Create the database and apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser for admin access:

bash
Copy code
python manage.py createsuperuser
Usage
Start the development server:

bash
Copy code
python manage.py runserver
Access the admin panel by visiting http://localhost:8000/admin/ and logging in with the superuser credentials.

Explore the API endpoints to manage content items:

Create Content: http://localhost:8000/api/create/ (POST)
Get Content List: http://localhost:8000/api/content/ (GET)
Get Content by ID: http://localhost:8000/api/content/<int:id>/ (GET)
Update or Delete Content: http://localhost:8000/api/content_action/<int:id>/ (PUT, DELETE)
