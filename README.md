# Django Rest Framework Project - Product API with Search

This project implements a simple Product API using Django Rest Framework (DRF).<br/>
The API interacts with a third-party service for search functionality via [algolia](https://www.algolia.com/)

## Requirements
- Python 3.12.8+
- Django 4.0+
- Django Rest Framework (DRF)
- Poetry (for managing dependencies)


## Setup Instructions
### 1. Clone the Repository<br/>
```bash
git clone git@github.com:Dejwwik/DRF-project.git
cd DRF-project
```

### 2. Install Dependencies
Install all dependencies using Poetry:
```bash
poetry install
```

### 3. Setup Environment Variables<br/>
Create a .env file in the root directory and add the following values:
```env
SECRET_KEY=SECRET_KEY
USERNAME=your_username
PASSWORD=your_password
APPLICATION_ID=ALGOLIA_APP_ID
API_KEY=ALGOLIA_ADMIN_API_KEY
```

### 4. Set up Django Superuser<br/>
To create a Django superuser (admin), run the following commands:
```bash
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```


### 5. Run the Server<br/>
To run the Django server, use the following command:
```bash
poetry run python manage.py runserver
```
Your application should now be live at http://127.0.0.1:8000.


### 6. Access the Admin Panel<br/>
Visit the Django Admin Panel at http://127.0.0.1:8000/admin and log in using the superuser credentials you created.

## API Consumption<br/>
### 1. Using Python Client (py_client)<br/>
To consume the API using Python, you can use py_client.py:

### 2. Using JS Client (js_client)<br/>
For consuming the API using a UI with JavaScript, you can use js_client.js
