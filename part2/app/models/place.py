#!/usr/bin/python3
"""
Place model module.

This module defines the Place class, which represents a property listing
in the HBnB application.
"""


from .base import BaseModel


class Place(BaseModel):
    """
    Represents a place (property listing) in the HBnB platform.

    A place:
        - Has one owner (User-like object with an id)
        - Can have multiple reviews (stored as review IDs)
        - Can have multiple amenities (stored as amenity IDs)
        - Has a title, optional description, price, and location (lat/long)
    """
    def __init__(
        self, owner, title="", description="", price=0,
        latitude=0, longitude=0
    ):
        """
        Initialize a new Place instance.

        Args:
            owner (object): Owner object (must have an 'id' attribute
            as UUID string).
            title (str): Place title (required, max 100 chars).
            description (str | None): Optional description.
            price (int | float): Price per night (must be > 0).
            latitude (int | float): Latitude (-90 to 90).
            longitude (int | float): Longitude (-180 to 180).

        Raises:
            TypeError: If a field type is invalid.
            ValueError: If a field value is invalid.
        """
        if not hasattr(owner, "id"):
            raise TypeError("Owner must have an 'id' attribute")

        self._validate_uuid(owner.id, "owner.id")

        if isinstance(title, str):
            title = title.strip()
        else:
            raise TypeError("Title must be a string")

        if title == "":
            raise ValueError("Title cannot be empty")
        if len(title) > 100:
            raise ValueError("Title must be <= 100 characters")

        if description is None:
            description = ""

        if not isinstance(description, str):
            raise TypeError("Description must be a string")

        description = description.strip()

        if not isinstance(price, (int, float)) or type(price) is bool:
            raise TypeError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be positive")

        if not isinstance(latitude, (int, float)) or type(latitude) is bool:
            raise TypeError("Latitude must be a number")
        if latitude < -90.0 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")

        if not isinstance(longitude, (int, float)) or type(longitude) is bool:
            raise TypeError("Longitude must be a number")
        if longitude < -180.0 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")

        super().__init__()

        self.owner_id = owner.id
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.review_ids = []  # List to store related review ids
        self.amenity_ids = []  # List to store related amenity ids

    def add_review(self, review):
        """
        Associate a review with this place.

        Args:
            review (object): Review-like object with an 'id' attribute.

        Adds the review ID to review_ids if not already present.
        """
        if not hasattr(review, "id"):
            raise TypeError("Review must have an 'id' attribute")
        self._validate_uuid(review.id, "review.id")
        if review.id not in self.review_ids:
            self.review_ids.append(review.id)

    def remove_review(self, review):
        """
        Remove an associated review from this place.

        Args:
            review (object): Review-like object with an 'id' attribute.
        """
        if not hasattr(review, "id"):
            raise TypeError("Review must have an 'id' attribute")
        self._validate_uuid(review.id, "review.id")
        if review.id in self.review_ids:
            self.review_ids.remove(review.id)

    def add_amenity(self, amenity):
        """
        Associate an amenity with this place.

        Args:
            amenity (object): Amenity-like object with an 'id' attribute.

        Adds the amenity ID to amenity_ids if not already present.
        """
        if not hasattr(amenity, "id"):
            raise TypeError("Amenity must have an 'id' attribute")
        self._validate_uuid(amenity.id, "amenity.id")
        if amenity.id not in self.amenity_ids:
            self.amenity_ids.append(amenity.id)

    def remove_amenity(self, amenity):
        """
        Remove an associated amenity from this place.

        Args:
            amenity (object): Amenity-like object with an 'id' attribute.
        """
        if not hasattr(amenity, "id"):
            raise TypeError("Amenity must have an 'id' attribute")
        self._validate_uuid(amenity.id, "amenity.id")
        if amenity.id in self.amenity_ids:
            self.amenity_ids.remove(amenity.id)
