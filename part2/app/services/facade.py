#!/usr/bin/python3
"""
This module provides the HBnBFacade class.

The facade acts as the single entry point between the Presentation layer
(API) and the application's core logic and persistence mechanisms.
"""


from app.persistence.repository import InMemoryRepository
from ..models.user import User
from ..models.review import Review


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
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

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

    # ---------- REVIEWS ----------
    def create_review(self, review_data):
        if not self.user_repo.get(review_data["user_id"]):
            raise ValueError("User not found")

        if not self.place_repo.get(review_data["place_id"]):
            raise ValueError("Place not found")

        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [
            review
            for review in self.review_repo.get_all()
            if review.place_id == place_id
        ]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None

        # prevent protected fields from being updated
        forbidden = {'id', 'created_at', 'updated_at', 'user_id', 'place_id',}
        clean_data = {k: v for k, v in review_data.items() if k not in forbidden}

        self.review_repo.update(review_id, clean_data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return None

        self.review_repo.delete(review_id)
        return True
