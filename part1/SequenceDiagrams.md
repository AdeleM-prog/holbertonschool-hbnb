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
alt Success
    BusinessLogic->>Database: Save user
    Database->>Database: Validate data
    Database-->>BusinessLogic: success
    BusinessLogic-->>API: 201 Created
    API-->>User: 201 Created
else User already exists
    BusinessLogic->>Database: Save user
    Database->>Database: Validate data
    Database-->>BusinessLogic: Failure
    BusinessLogic-->>API: 409 Conflict
    API-->>User: 409 Conflict
else Invalid data
    BusinessLogic-->>API: 400 Bad Request
    API-->>User: 400 Bad Request
end
```

---

## 2. Place Creation:
```mermaid
sequenceDiagram

```

---

## 3. Review Submission:
```mermaid
sequenceDiagram

```

---

## 3. Fetching a List of Places:
```mermaid
sequenceDiagram

```
