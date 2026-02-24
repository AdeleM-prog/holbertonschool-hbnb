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

    # ---------- USERS ----------
    def create_user(self, user_data):
        """
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        """
        return self.user_repo.get(user_id)

    def get_users(self):
        """
        """
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        """
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        """
        """
        user = self.user_repo.get(user_id)
        if not user:
            return None

        # prevent protected fields from being updated
        forbidden = {'id', 'created_at', 'updated_at', 'is_admin', 'place_ids', 'review_ids'}
        clean_data = {k: v for k, v in user_data.items() if k not in forbidden}

        self.user_repo.update(user_id, clean_data)
        return self.user_repo.get(user_id)
