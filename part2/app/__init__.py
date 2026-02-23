#!/usr/bin/python3
"""
This module provides the create_app function
It defines the Flask application factory used to initialize the HBnB API
and configure Flask-RESTx.
"""


from flask import Flask
from flask_restx import Api


def create_app():
    """
    Application factory function.

    Creates and configures the Flask application instance,
    initializes the Flask-RESTx API, and prepares the
    structure for registering namespaces and endpoints.

    Returns:
        Flask: The configured Flask application instance.
        """
    app = Flask(__name__)
    api = Api(
        app, version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
        )

    # Placeholder for API namespaces (endpoints will be added later)
    # Additional namespaces for places, reviews, and amenities
    # will be added later.

    return app
