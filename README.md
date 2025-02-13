# Rest Framework API for Author Management

## Overview

This project is a RESTful API built using Django and Django REST Framework, aimed at managing authors in a database. It provides a simple way to create, read, update, and delete author records, embodying the principles of CRUD functionality.

## Technologies Used

Backend Framework: Django 5.1.6
Database: PostgreSQL (or any other preferred relational database)
Version Control: Git and GitHub for source code management
Image Processing: Pillow for handling image uploads
API Documentation: Swagger or similar documentation tools (optional)
APIs: Possible integration with email service providers for notifications

## Features

CRUD Functionality:

Create: Add new author records to the database.
Read: Retrieve information about authors, including all authors or individual author details.
Update: Modify existing author information.
Delete: Remove authors from the database.
Image Upload Support: Allows uploading of author profile photos.

Input Validation: Ensures proper formatting for email and phone number fields.

Ordering: Authors are automatically ordered by the creation date in descending order.

API Authentication: (Optional) Secure the API using token-based authentication.

## Requirements

Python 3.6 or higher
Django 4x or higher
Django REST Framework 3.x or higher
Pillow (for image handling)

Installation
Clone the repository:
git clone https://github.com/cwalton133/restframe_Api.git

Navigate to the project directory:
cd restframe_api

Create a virtual environment(recommended)
python -m venv venv

## Ativate your Environement

source venv/bin/activate # On Windows use
`venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Apply the migrations to create the database tables:
python manage.py migrate

Create a superuser to access the Django admin (optional):
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Navigate to http://127.0.0.1:8000/ in your web browser to access the API.

## API Enpoints:

Authors
Base URL: /api/authors/

GET /api/authors/ - Retrieve a list of all authors.

POST /api/authors/ - Create a new author.

Request Body:
{
"first_name": "John",
"last_name": "Doe",
"other_name": "Johnny",
"email": "john.doe@example.com",
"phone_number": "+123456789",
"mobile_number": "+987654321",
"photo": "base64_encoded_image"
}

GET /api/authors/{id}/ - Retrieve a specific author by ID.

PUT /api/authors/{id}/ - Update a specific author's information.

Request Body:
{
"first_name": "Jane",
"last_name": "Doe",
"other_name": "",
"email": "jane.doe@example.com",
"phone_number": "+123456780",
"mobile_number": "+987654320",
"photo": "base64_encoded_image"
}

DELETE /api/authors/{id}/ - Delete a specific author by ID.

## Model Definitions:

The Author model is defined with the following fields:
id: Auto-incrementing primary key.
first_name: First name of the author (max length 55).
last_name: Last name of the author (max length 55).
other_name: Other name or nickname (optional).
email: Email address (valid email format).
phone_number: Primary phone number (max length 20).
mobile_number: Mobile number (max length 20).
photo: Profile photo (uploaded to the Author directory).
created_at: Timestamp for when the author was created.

## Meta Options

The authors are ordered by creation date in descending order.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledements:

Django
Django REST Framework
PostgreSQL
Pillow

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## Contact

For any questions or feedback, please contact:

Charles Walton - cwalton1335@gmail.com
GitHub: cwalton133
Thank you for checking out the Products Application!
