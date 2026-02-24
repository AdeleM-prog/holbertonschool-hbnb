#!/usr/bin/python3


from app.model.base import BaseModel
from app.models.amenity import Amenity


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if isinstance(title, str):
            title = title.strip()
        else:
            raise TypeError("Title must be a string")
        if title=="":
            raise ValueError("Title cannot be empty")
        if len(title) > 100:
            raise ValueError("Title must be <= 100 characters")
        self.title = title

        if isinstance(description, str) or description is None:
            self.description = description
        else:
            raise TypeError("Description must be a string or None")

        if isinstance(price, (int, float)):
            if isinstance(price, bool):
                raise TypeError("Price must be a number")
            if price <= 0:
                raise ValueError("Price must be positive")
            self.price = price
        else:
            raise TypeError("Price must be a number")

        if isinstance(latitude, (int, float)):
            if isinstance(latitude, bool):
                raise TypeError("Latitude must be a number")
            if -90.0 <= latitude <= 90:
                self.latitude = latitude
            else:
                raise ValueError("Latitude must be between -90 and 90")
        else:
            raise TypeError("Latitude must be a number")

        if isinstance(longitude, (int, float)):
            if isinstance(longitude, bool):
                raise TypeError("Longitude must be a number")
            if -180.0 <= longitude <= 180:
                self.longitude = longitude
            else:
                raise ValueError("Longitude must be between -180 and 180")
        else:
            raise TypeError("Longitude must be a number")

        if isinstance(owner, User):
            self.owner = owner
        else:
            raise TypeError("Owner must be an instance of User class")

        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
    def add_review(self, review):
        """Add a review to the place."""
        if isinstance(review, Review):
            self.reviews.append(review)
        else:
            raise TypeError("Review must be an instance of Review")

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if isinstance(amenity, Amenity):
            pass
        else:
            raise TypeError("Amenities must be an instance of Amenity")
        for element in self.amenities:
            if amenity.id == element.id:
                raise ValueError("Amenity already exists")
        self.amenities.append(amenity)
        

