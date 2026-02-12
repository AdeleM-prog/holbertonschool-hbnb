# Holberton School - HBnB
### Sequence Diagrams for API calls of the HBnB Evolution application

---

## 1. User Registration:
```mermaid
sequenceDiagram

participant User
participant API
participant BusinessLogic
participant Database

User->>API: Register account
API->>BusinessLogic: Validate and process registration
BusinessLogic->>BusinessLogic: Validate User data

alt Invalid data
    BusinessLogic-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else Valid data
    BusinessLogic->>Database: Save User
    Database->>Database: Execute INSERT

    alt User already exists
        Database-->>BusinessLogic: Insert failed (duplicate email)
        BusinessLogic-->>API: 409 Conflict
        API-->>User: 409 Conflict
        
    else Success
        Database-->>BusinessLogic: Insert OK
        BusinessLogic-->>API: 201 Created + UserDTO
        API-->>User: 201 Created + UserDTO
    end
end
```

---

## 2. Place Creation:
```mermaid
sequenceDiagram

participant User
participant API
participant BusinessLogic
participant Database

User->>API: Create Place
API->>BusinessLogic: Validate and process creation
BusinessLogic->>BusinessLogic: Validate Place data

alt Invalid data
    BusinessLogic-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else User not connected
    BusinessLogic-->>API: 401 Unauthorized
    API-->>User: 401 Unauthorized

else User not allowed
    BusinessLogic-->>API: 403 Forbidden
    API-->>User: 403 Forbidden

else Valid data
    BusinessLogic->>Database: Save Place
    Database->>Database: Execute INSERT

    alt DB error
        Database-->>BusinessLogic: Insert failed
        BusinessLogic-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
    
    else Success
        Database-->>BusinessLogic: Insert OK
        BusinessLogic-->>API: 201 Created + PlaceDTO
        API-->>User: 201 Created + PlaceDTO
    end
end
```

---

## 3. Review Submission:
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Create Review
API->>BusinessLogic: Validate and process creation
BusinessLogic->>BusinessLogic: Validate Review data

alt Invalid data
    BusinessLogic-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else User not connected
    BusinessLogic-->>API: 401 Unauthorized
    API-->>User: 401 Unauthorized

else User not allowed
    BusinessLogic-->>API: 403 Forbidden
    API-->>User: 403 Forbidden

else Place not found
    BusinessLogic-->>API: 404 Not Found
    API-->>User: 404 Not Found

else Valid data
    BusinessLogic->>Database: Save Review
    Database->>Database: Execute INSERT

    alt DB error
        Database-->>BusinessLogic: Insert failed
        BusinessLogic-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
    
    else Success
        Database-->>BusinessLogic: Insert OK
        BusinessLogic-->>API: 201 Created + ReviewDTO
        API-->>User: 201 Created + ReviewDTO
    end
end
```

---

## 3. Fetching a List of Places:
```mermaid
sequenceDiagram

participant User
participant API
participant BusinessLogic
participant Database

User->>API: Make a research
API->>BusinessLogic: Validate and fetching
BusinessLogic->>BusinessLogic: Validate filters

alt Invalid filters
    BusinessLogic-->>API: 400 Bad Request
    API-->>User: 400 Bad Request

else Valid data
    BusinessLogic->>Database: Make query
    Database->>Database: Execute SELECT

    alt DB error
        Database-->>BusinessLogic: Query failed
        BusinessLogic-->>API: 500 Internal Server Error
        API-->>User: 500 Internal Server Error
    
    else Success
        Database-->>BusinessLogic: Insert OK
        BusinessLogic-->>API: 200 PlacesDTO
        API-->>User: 200 PlacesDTO
    end
end
```
