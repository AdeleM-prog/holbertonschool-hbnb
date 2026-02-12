# Holberton School - HBnB
## Sequence Diagrams for API calls of the HBnB Evolution application

---

## 1. User Registration:
```mermaid
sequenceDiagram

participant User
participant API
participant BL as BusinessLogic<br/>(UserService)
participant DB as Database

User->>API: Register account
API->>BL: Validate and process registration
BL->>BL: Validate User data

alt Invalid data
    BL-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else Valid data
    BL->>DB: Save User
    DB->>DB: Execute INSERT

    alt User already exists
        DB-->>BL: Insert failed (duplicate email)
        BL-->>API: 409 Conflict
        API-->>User: 409 Conflict
    
    else DB error
        DB-->>BL: Insert failed
        BL-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
        
    else Success
        DB-->>BL: Insert OK
        BL-->>API: 201 Created + UserDTO
        API-->>User: 201 Created + UserDTO
    end
end
```

---

## Description
This sequence diagram illustrates the process of user registration, from the client request to database persistence and response delivery.

### Business Rules
- User email must be unique.
- User data must be valid before persistence.
- Registration fails if the email already exists.

### Possible Outcomes
- 201 Created: user successfully created.
- 400 Bad Request: invalid user data.
- 409 Conflict: email already exists.
- 500 Internal Server Error: database failure.

---

## 2. Place Creation:
```mermaid
sequenceDiagram

participant User
participant API
participant BL as BusinessLogic<br/>(PlaceService)
participant DB as Database

User->>API: Create Place
API->>BL: Validate and process creation
BL->>BL: Validate Place data

alt Invalid data
    BL-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else User not connected
    BL-->>API: 401 Unauthorized
    API-->>User: 401 Unauthorized

else User not allowed
    BL-->>API: 403 Forbidden
    API-->>User: 403 Forbidden

else Valid data
    BL->>DB: Save Place
    DB->>DB: Execute INSERT

    alt DB error
        DB-->>BL: Insert failed
        BL-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
    
    else Success
        DB-->>BL: Insert OK
        BL-->>API: 201 Created + PlaceDTO
        API-->>User: 201 Created + PlaceDTO
    end
end
```

---

## Description
This diagram shows how a place is created and stored after validation and authorization checks.

### Business Rules
- Only authenticated users can create places.
- Each place must have valid data.
- The creator becomes the owner of the place.

### Possible Outcomes
- 201 Created: place successfully created.
- 400 Bad Request: invalid place data.
- 401 Unauthorized: user not authenticated.
- 403 Forbidden: user not allowed to create a place.
- 500 Internal Server Error: database failure.

---

## 3. Review Submission:
```mermaid
sequenceDiagram
participant User
participant API
participant BL as BusinessLogic<br/>(ReviewService)
participant DB as Database

User->>API: Create Review
API->>BL: Validate and process creation
BL->>BL: Validate Review data

alt Invalid data
    BL-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else User not connected
    BL-->>API: 401 Unauthorized
    API-->>User: 401 Unauthorized

else User not allowed
    BL-->>API: 403 Forbidden
    API-->>User: 403 Forbidden

else Place not found
    BL-->>API: 404 Not Found
    API-->>User: 404 Not Found

else Valid data
    BL->>DB: Save Review
    DB->>DB: Execute INSERT

    alt DB error
        DB-->>BL: Insert failed
        BL-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
    
    else Success
        DB-->>BL: Insert OK
        BL-->>API: 201 Created + ReviewDTO
        API-->>User: 201 Created + ReviewDTO
    end
end
```

---

## Description
This diagram illustrates the submission of a review for a place.

### Business Rules
- Only authenticated users can submit reviews.
- A user cannot review their own place.
- A review must target an existing place.
- Review data must be valid before saving.

### Possible Outcomes
- 201 Created: review successfully saved.
- 400 Bad Request: invalid review data.
- 401 Unauthorized: user not authenticated.
- 403 Forbidden: user not allowed to review this place.
- 404 Not Found: place does not exist.
- 500 Internal Server Error: database failure.

---

## 4. Fetching a List of Places:
```mermaid
sequenceDiagram

participant User
participant API
participant BL as BusinessLogic<br/>(PlaceService)
participant DB as Database

User->>API: Get places
API->>BL: Validate filters and fetch places
BL->>BL: Validate filters

alt Invalid filters
    BL-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else Valid filters
    BL->>DB: Query places
    DB->>DB: Execute SELECT

    alt DB error
        DB-->>BL: Query failed
        BL-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
    
    else Success
        DB-->>BL: Query OK
        BL-->>API: 200 OK + PlacesDTO[]
        API-->>User: 200 OK + PlacesDTO[]
    end
end
```

---

## Description
This diagram shows how a list of places is fetched based on search filters.

### Business Rules
- Search filters must be valid.
- Results may be empty if no places match filters.

### Possible Outcomes
- 200 OK: places (or an empty list) successfully returned.
- 400 Bad Request: invalid search filters.
- 500 Internal Server Error: database failure.
