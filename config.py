""" module for server config options"""
import os


# Setup an environment variable for the jwt secret key.
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
