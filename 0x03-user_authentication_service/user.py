#!/usr/bin/env python3
"""
This module contains the User model for the
users table in the database
"""
import sqlalchemy as s
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    """
    Defines the User model for the users table
    """
    __tablename__ = "users"

    id = s.Column(s.Integer, primary_key=True)
    username = s.Column(s.String(250), nullable=False)
    email = s.Column(s.String(250), nullable=False)
    hashed_password = s.Column(s.String(250), nullable=False)
    session_id = s.Column(s.String(250), nullable=True)
    reset_token = s.Column(s.String(250), nullable=True)
