# Holberton School - HBnB
### Class Diagram for Business Logic Layer of the HBnB Evolution application

---

```mermaid
classDiagram

class User {
    +id: UUID4
    +created_at: datetime
    +updated_at: datetime

    +first_name: string
    +last_name: string
    +email: string
    +password: string
    +is_admin: bool

    +register() void
    +update_profile() void
    +delete_profile() void
}

class Place {
    +id: UUID4
    +created_at: datetime
    +updated_at: datetime

    +title: string
    +description: string
    +price: float
    +latitude: float
    +longitude: float

    +create() void
    +update() void
    +delete() void
    +list() void
}

class Review {
    +id: UUID4
    +created_at: datetime
    +updated_at: datetime

    +rating: int
    +comment: string

    +create() void
    +update() void
    +delete() void
    +list() void
}

class Amenity {
    +id: UUID4
    +created_at: datetime
    +updated_at: datetime

    +name: string
    +description: string

    +create() void
    +update() void
    +delete() void
    +list() void
}

Place "0..*" --> "1" User : owner
Amenity "0..*" --> "0..*" Place : amenities
Place "1" --> "0..*" Review : reviews
Review "0..*" --> "1" User : author
```

---

### **User:** Represents a platform user who can own places and write reviews.
- Stores personal information and authentication data.
- Can register, update, or delete their profile.
- May have administrator privileges.
- Can own multiple places and write multiple reviews.

### **Place:** Represents a property listed by a user.
- Contains descriptive information, pricing, and geographic location.
- Each place is owned by one user.
- A place can have multiple amenities and reviews.
- Supports creation, update, deletion, and listing operations.

### **Review:** Represents feedback left by a user for a place.
- Contains a rating and a comment.
- Each review is linked to one user (author) and one place.
- A place can have multiple reviews.
- Supports creation, update, deletion, and listing operations.

### **Amenity:** Represents a service or feature available in a place.
- Contains a name and description.
- Amenities can be shared across multiple places.
- Supports creation, update, deletion, and listing operations.

**Every instance of HBnB entities also includes:**
- A unique identifier in UUID4 format.
- The datetime of creation of the instance.
- The datetime of the last update of the instance. If no update has occurred, it is identical to the creation datetime.

---

### **Entity Relationships**
- **User–Place:** A user can own multiple places, while each place has exactly one owner.
- **Place–Review:** A place can have multiple reviews, but each review refers to a single place.
- **User–Review:** A user can write multiple reviews, but each review has only one author.
- **Place–Amenity:** Places can include multiple amenities, and amenities can be shared by multiple places.

These relationships define how core entities interact within the business logic layer and ensure consistent data connections across the application.
