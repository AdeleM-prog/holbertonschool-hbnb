In the README.md file, write a brief overview of the project setup:
Describe the purpose of each directory and file.
Include instructions on how to install dependencies and run the application.

# HBnB Evolution – Part 2
## Business Logic & API Layer

## 1. Overview

This part of the HBnB Evolution project implements the core Business Logic and the REST API layer of the application.

The goal is to provide a clean architecture separating:

- Business logic
- API endpoints
- Data models
- Application configuration

The API exposes resources such as users, places, reviews, and amenities, following REST principles.
<br>
<br>

---
## 2. Project Structure

    ```text
    hbnb/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── v1/
    │   │       ├── __init__.py
    │   │       ├── users.py
    │   │       ├── places.py
    │   │       ├── reviews.py
    │   │       ├── amenities.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── user.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   ├── amenity.py
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── facade.py
    │   ├── persistence/
    │       ├── __init__.py
    │       ├── repository.py
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ```

---
## Directories & Files
<br>

### 🔹 app/__init__.py

Creates the Flask application using the application factory pattern.

Responsibilities:
- Initialize Flask
- Configure Flask-RESTx
- Register API namespaces
- Prepare the application for modular expansion
<br>
<br>
### 🔹 app/api/v1/

Contains REST API namespaces. Each file defines endpoints for a resource:

users.py: User registration and management  
places.py: Manage places  
reviews.py: Manage reviews  
amenities.py: Manage amenities  

Namespaces are registered under:

/api/v1/<resource>

Example:
/api/v1/users
<br>
<br>
### 🔹 app/models/

Defines the core business entities.

**base.py**

BaseModel class providing:
- UUID identifier
- created_at / updated_at timestamps
- shared logic

**user.py**
Represents a platform user.

**place.py**
Represents a rental place.

**review.py**
Represents user reviews.

**amenity.py**
Represents amenities associated with places.
<br>
<br>

### 🔹 app/services/

Contains the Business Logic layer.
<br>
<br>

**facade.py**

Implements a Facade pattern that:
- centralizes business operations
- isolates API from model logic
- simplifies service orchestration  
This layer ensures separation of concerns and prepares future database integration.
<br>
<br>
### 🔹 run.py
Application entry point. Used to start the Flask server.
<br>
<br>
### 🔹 requirements.txt
Lists required dependencies.
<br>
<br>

---
## Installation  
1️⃣ Clone the repository  
git clone <https://github.com/AdeleM-prog/holbertonschool-hbnb.git>

2️⃣ In the requirements.txt file, list the Python packages needed for the project:
```bash   
flask  
flask-restx  
 ```
3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
 ```

▶️ Running the Application 
```bash 
python run.py
 ```

---
<br>
API documentation is available at:

```bash
http://localhost:5000/api/v1/  
 ```

<br>

### Available Endpoints 

<br>

**Users**

POST /api/v1/users  
GET /api/v1/users/<id>  
PUT /api/v1/users/<id>  

**Places**

POST /api/v1/places  
GET /api/v1/places/<id>  
PUT /api/v1/places/<id>  

**Reviews**

POST /api/v1/reviews  
GET /api/v1/reviews/<id>  
PUT /api/v1/reviews/<id>  
DELETE /api/v1/reviews/<id>  

**Amenities**

PUT /api/v1/amenities/<id>  
GET /api/v1/amenities/<id>  

**Validation Rules**

Business entities enforce strict validation:

- Required fields must be provided
- Types are verified
- String length limits enforced
- Invalid data raises exceptions
<br>
This ensures data integrity before persistence.

---
### Architectural Principles

This project follows:

✔ Application Factory Pattern  
✔ RESTful API design  
✔ Separation of concerns  
✔ Facade pattern for business logic  
✔ Modular architecture  
✔ Validation at model level  

---

## 3. Authors

Project developed as part of the Holberton School curriculum.

Team:
- Adele Megelink: https://github.com/AdeleM-prog
- Felix Besançon: https://github.com/FelixBesancon