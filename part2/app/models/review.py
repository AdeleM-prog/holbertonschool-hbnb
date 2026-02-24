#!/usr/bin/python3
"""
Review model module.

This module defines the Review class, which represents a review
left by a user for a place in the HBnB application.
"""


import uuid
from .base import BaseModel


class Review(BaseModel):
    """
    Represents a review of a place in the HBnB platform.

    A review:
        - Has one author (User)
        - Refers to one place (Place)
        - Contains a rating (1 to 5)
        - Contains a textual comment
    """

    def __init__(self, author, place, rating=0, comment=""):
        """
        Initialize a new Review instance.

        Args:
            author (object): The user object who writes the review.
            place (object): The place object being reviewed.
            rating (int): Rating score between 1 and 5.
            comment (str): Review comment (minimum length required).

        Raises:
            TypeError: If types are invalid.
            ValueError: If validation rules are violated.
        """
        if not hasattr(author, "id"):
            raise TypeError("Author must have an 'id' attribute")

        self._validate_uuid(author.id, "author.id")

        if not hasattr(place, "id"):
            raise TypeError("Place must have an 'id' attribute")

        self._validate_uuid(place.id, "place.id")

        if not isinstance(rating, int):
            raise TypeError("Rating must be an integer")

        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        if not isinstance(comment, str):
            raise TypeError("Comment must be a string")

        cleaned_comment = comment.strip(" ,;:!?./")

        if len(cleaned_comment) < 15:
            raise ValueError(
                "Comment must be at least 15 characters long"
            )

        super().__init__()

        self.author_id = author.id
        self.place_id = place.id
        self.rating = rating
        self.comment = cleaned_comment

    @staticmethod
    def _validate_uuid(value, field_name):
        """
        Validate that a given string is a valid UUID.

        Args:
            value (str): The value to validate.
            field_name (str): Field name for error reporting.

        Raises:
            ValueError: If the value is not a valid UUID.
        """
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")

        try:
            uuid.UUID(value)
        except ValueError as exc:
            raise ValueError(
                f"{field_name} must be a valid UUID"
            ) from exc
