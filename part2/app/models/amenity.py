#!/usr/bin/python3

from .base import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
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
