
# Content Management System

This is a Django-based Content Management System (CMS) project that allows users to create, view, update, and delete content items along with feature to add multiple categories in content item.



## Table of Content

* Installation
* Usage
* Test Coverage


## Installation

1. Clone the repository:

```bash
  git clone https://github.com/althafMuhammedUmer/ContentManagementSystem.git
  cd ContentManagementSystem
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Create the database and apply migrations:

```bash
python manage.py migrate
```
5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

    
## Usage/Examples

1. Start the development server:
```bash
python manage.py runserver
```
2. Access the admin panel by visiting http://localhost:8000/admin/ and logging in with the superuser credentials.

3. Explore the API endpoints to manage content items:

* Create Content: http://localhost:8000/api/create/ (POST)
* Get Content List: http://localhost:8000/api/content/ (GET)
* Get Content by ID: http://localhost:8000/api/content/<int:id>/  (GET)
* Update or Delete Content: http://localhost:8000/api/content_action/<int:id>/ (PUT, DELETE)



## Running Tests

This project includes unit tests to ensure its functionality. You can generate test coverage reports by running the following command:

```bash
  coverage run --source='.' manage.py test
```

To see the test report:
```bash
coverage report
```


