# real_estate_management

Developed a Real Estate Management System using Django and Django REST Framework. This system will handle tenant profiles, property, units.

# Getting Started
# Prerequisites

**Technology** 
# Backend
- Python 3.11.6
- Django 4.2.7
- django-rest-knox 4.2.0
- Git (for cloning the repository)
# Frontend 
- Django Template
- jquery
- Boostrap
- HTML And CSS
# DataBase
- SQLite

# **Libraries Used**

- **Django Rest Knox**:  is a popular third-party package called "django-rest-knox" that provides token authentication for Django REST Framework. Token-based authentication is stateless, meaning the server does not need to store any information about the client's state. Token-based authentication is scalable as it doesn't rely on server-side sessions. Each request contains the necessary information for authentication.
- Knox tokens are a secure way to transmit information between parties, and they are commonly used for authentication in web applications.

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the Model-View-Controller (MVC) architectural pattern and includes an Object-Relational Mapping (ORM) system for database interactions. In your project, Django serves as the foundation for building web applications.

- **Djangorestframework**: Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django applications. It is an extension of Django that makes it easy to build, test, and deploy RESTful APIs. DRF includes serializers for data handling, class-based views for defining API endpoints, and authentication mechanisms. It simplifies the process of building robust and scalable APIs.

- Perpare form validation using jquery and used some jquery libraries (select2,sweetalert2,datatable,feather icons)
  
# Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Larans17/real_estate_management.git
   
2. Create the environment:

   ```bash
   py -m venv venv
   
3. Activate the environnment:
   
      ```bash
     .\venv\Scripts\activate
  
4. Install the requirements:

   ```bash
   pip install -r requirements.txt
   
5. Run Migrations:

   ```bash
   python manage.py makemigrations
   
   python manage.py migrate

6. Create Super User:

   ```bash
   python manage.py createsuperuser
      
7. Run the code:

   ```bash
   python manage.py runserver
   
