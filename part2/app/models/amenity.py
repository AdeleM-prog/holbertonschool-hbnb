#!/usr/bin/python3

from .base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, description=None):
        super().__init__()

        if isinstance(name, str):
            name = name.strip()
            if name == "":
                raise ValueError("Name cannot be empty")
            if len(name) <= 50:
                self.name = name
            else:
                raise ValueError("Name must be 50 characters maximum")
        else:
            raise TypeError("Name must be a string")
        
        if description is None:
            self.description = description
        else:
            if isinstance(description, str):
                if len(description) <= 150:
                    self.description = description
                else:
                    raise ValueError("Description must be maximum 150 characters")
            else:
                raise TypeError("Description must be a string")

