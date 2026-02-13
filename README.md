# Holberton School - HBnB 
## Technical Documentation of the HBnB Evolution application

HBnB Evolution is a simplified AirBnB-like platform designed to manage users, places, amenities, and reviews.

This repository contains the **technical documentation** describing the architecture and core design of the application before implementation.

The goal of this phase is to define **how the system is structured and how components interact**, ensuring a clear blueprint for development.

---

## 1. Project Overview

HBnB Evolution allows users to:

- Register and manage accounts
- Create and manage places
- Add amenities to places
- Submit reviews for places
- Search and browse available places

The documentation covers:

- Application architecture
- Business entities and relationships
- Interaction flows between components

---

## 2. Architecture

The application follows a **layered architecture**, separating responsibilities into three main layers:

### Presentation Layer:
Handles user/API interactions.
- API endpoints
- Controllers
- Request/response handling

### Business Logic Layer:
Contains application rules and core domain logic.
- Facade entry point
- Domain models
- Services implementing business rules

### Persistence Layer:
Responsible for data storage.
- Repositories
- Database access

Typical flow:

Client → API → Business Logic → Repositories → Database


Responses follow the reverse path back to the client.

---

## 3. Business Entities

Core entities modeled in the system:

### User:
Represents a platform user.
- Can own places
- Can submit reviews
- May have admin privileges

### Place:
Represents a property listing.
- Owned by a user
- Can include amenities
- Can receive reviews

### Review:
Feedback left by a user for a place.
- Linked to both user and place

### Amenity:
Represents services/features available in places.

All entities share:
- UUID identifier
- Creation timestamp
- Update timestamp

---

## 4. API Interaction Flows

Sequence diagrams describe how the system handles major API operations:

1. User Registration
2. Place Creation
3. Review Submission
4. Fetching Places

Each flow illustrates:
- Validation steps
- Authorization checks
- Database interaction
- Success and error responses

---

## 5. Documentation Structure

The repository includes:

part1/
├── package diagram (architecture)
├── class diagram (business models)
└── sequence diagrams (API flows)

These diagrams provide the foundation for later implementation phases.

---

## 6. Objective

This documentation ensures that:
- Architecture is clearly defined
- Responsibilities are separated
- Development can proceed consistently
- Future extensions remain manageable

---

## 7. Authors

Project developed as part of the Holberton School curriculum.

Team:
- Adele Megelink: https://github.com/AdeleM-prog
- Felix Besançon: https://github.com/FelixBesancon
