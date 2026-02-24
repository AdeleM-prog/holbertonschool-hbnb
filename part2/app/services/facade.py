#!/usr/bin/python3
"""
This module provides the HBnBFacade class.

The facade acts as the single entry point between the Presentation layer
(API) and the application's core logic and persistence mechanisms.
"""


from app.persistence.repository import InMemoryRepository
from ..models.user import User


class HBnBFacade:
    """
    Facade class that centralizes access to the application's
    business logic and repositories.

    This class acts as an intermediary between the Presentation
    layer (API) and the underlying persistence layer, simplifying
    communication and enforcing separation of concerns.
    """
    def __init__(self):
        """
        Initialize the facade and its in-memory repositories.

        Each entity type (User, Place, Review, Amenity)
        is managed by a dedicated repository instance.
        """
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        Create a new user.

        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        """
        return self.user_repo.get_by_attribute('email', email)
