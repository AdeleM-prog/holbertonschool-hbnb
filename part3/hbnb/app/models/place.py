from app import db
from app.models.base_model import BaseModel
from .user import User

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1024))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, title, price, latitude, longitude, description=None):
#        super().__init__()
        self.set_title(title)
        self.set_price(price)
        self.set_latitude(latitude)
        self.set_longitude(longitude)
        self.set_description(description)
#        self.set_owner(owner)
#        self.reviews = []  # List to store related reviews
#        self.amenities = []  # List to store related amenities
#
#    @property
#    def title(self):
#        return self.__title
    
#    @title.setter
    def set_title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        super().is_max_length('title', value, 100)
#        self.__title = value
#
#    @property
#    def price(self):
#        return self.__price
    
#    @price.setter
    def set_price(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be positive.")
#        self.__price = value
#
#    @property
#    def latitude(self):
#        return self.__latitude
    
#    @latitude.setter
    def set_latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")
        super().is_between("latitude", value, -90, 90)
#        self.__latitude = value
#    
#    @property
#    def longitude(self):
#        return self.__longitude
    
#    @longitude.setter
    def set_longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")
        super().is_between("longitude", value, -180, 180)
#        self.__longitude = value
#
#    @property
#    def owner(self):
#        return self.__owner
    
#    @owner.setter
#    def set_owner(self, value):
#        if not isinstance(value, User):
#            raise TypeError("Owner must be a user instance")
#        self.__owner = value
#
#    def add_review(self, review):
#        """Add a review to the place."""
#        self.reviews.append(review)
#    
#    def delete_review(self, review):
#        """Add an amenity to the place."""
#        self.reviews.remove(review)
#
#    def add_amenity(self, amenity):
#        """Add an amenity to the place."""
#        self.amenities.append(amenity)
#
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
#            'owner_id': self.owner.id
        }
#    
#    def to_dict_list(self):
#        return {
#            'id': self.id,
#            'title': self.title,
#            'description': self.description,
#            'price': self.price,
#            'latitude': self.latitude,
#            'longitude': self.longitude,
#            'owner': self.owner.to_dict(),
#            'amenities': self.amenities,
#            'reviews': self.reviews
#        }
