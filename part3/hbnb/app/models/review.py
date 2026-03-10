from app import db
from app.models.base_model import BaseModel


class Review(BaseModel):
    """
    SQLAlchemy model representing a review in the HBnB application.

    This model defines the core attributes of a review, including its text
    content and rating.

    The class inherits from BaseModel, which provides common attributes
    and functionality such as:
        - id (UUID primary key)
        - created_at timestamp
        - updated_at timestamp
        - validation helpers (e.g. is_max_length, is_between)

    Relationships with other entities (User, Place) are intentionally
    not implemented at this stage and will be added in later tasks.
    """

    __tablename__ = 'reviews'

    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating):
        """
        Initialize a Review instance.

        Args:
            text (str): Review content. Must be a non-empty string with
                        a maximum length of 1024 characters.
            rating (int): Review rating. Must be an integer between 1 and 5.
        """
        self.set_text(text)
        self.set_rating(rating)
#       self.place = place
#       self.user = user
#
#   @property
#   def text(self):
#       return self.__text

#   @text.setter
    def set_text(self, value):
        """
        Validate and assign the review text.

        Args:
            value (str): Review content.

        Raises:
            ValueError: If the text is empty.
            TypeError: If the text is not a string.
        """
        if not value:
            raise ValueError("Text cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        super().is_max_length('Text', value, 1024)
        self.text = value
#
#   @property
#   def rating(self):
#       return self.__rating

#   @rating.setter
    def set_rating(self, value):
        """
        Validate and assign the review rating.

        Args:
            value (int): Rating value.

        Raises:
            TypeError: If the rating is not an integer.
            ValueError: If the rating is not between 1 and 5.
        """
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError("Rating must be an integer")
        super().is_between('Rating', value, 1, 5)
        self.rating = value
#
#   @property
#   def place(self):
#       return self.__place
#
#   @place.setter
#   def place(self, value):
#       if not isinstance(value, Place):
#           raise TypeError("Place must be a place instance")
#       self.__place = value
#
#   @property
#   def user(self):
#       return self.__user
#
#   @user.setter
#   def user(self, value):
#       if not isinstance(value, User):
#           raise TypeError("User must be a user instance")
#       self.__user = value

    def to_dict(self):
        """
        Serialize the Review object into a dictionary.

        Returns:
            dict: A dictionary containing the review attributes.
        """
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
        }
#           'place_id': self.place.id,
#           'user_id': self.user.id
