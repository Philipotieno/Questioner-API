""" function to perform validations"""
import re
from flask import jsonify


def validate_register(data):
    # validate firstname
    if validate_firstname(data):
        return validate_firstname(data)

    # validate lastname
    if validate_lastname(data):
        return validate_lastname(data)

    # validate username
    if validate_username(data):
        return validate_username(data)

    # validate phone
    if validate_phone(data):
        return validate_phone(data)

    # validate email
    if validate_email(data):
        return validate_email(data)

    # validate password
    if validate_password(data):
        return validate_password(data)

def validate_meetup(data):
    #validate firstname
    if validate_topic(data):
        return validate_topic(data)

def validate_firstname(data):
    """Validate firstname"""
    if not re.match(r'^[a-zA-Z]', data['firstname']):
        msg = "Firstname should have letters and should be 3 or more characters long"
        return jsonify({'message': msg}), 400

def validate_lastname(data):
    """Validate firstname"""
    if not re.match(r'^[a-zA-Z]', data['firstname']):
        msg = "Lastname should have letters and should be 3 or more characters long"
        return jsonify({'message': msg}), 400

def validate_username(data):
    """Validate username"""
    if not re.match(r'^[a-zA-Z0-9]{5,15}$', data['username']):
        msg = "Username should have letters or numbers or a combination of both and should be 5 or more characters long"
        return jsonify({'message': msg}), 400


def validate_email(data):
    """Validate email"""
    if not re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$', data['email']):
        msg = "Please input a valid email!"
        return jsonify({'message': msg}), 400

def validate_phone(data):
    """Validate phone_nu,ber"""
    if not re.match(r'^[07]\d{9}$', data['phone_number']):
        msg = "Please input a valid phone number of the format 0703473377!"
        return jsonify({'message': msg}), 400

def validate_password(data):
    """Validate password"""
    if not re.match(r'^[\w\W]{6,}$', data['password']):
        msg = "Password must be at least 6 characters long"
        return jsonify({'message': msg}), 400

def validate_topic(data):
    """Validate topic"""
    if not re.match(r'^[a-zA-Z0-9]{3,15}$', data['topic']):
        msg = "Username should have letters or numbers or a combination of both and should be 5 or more characters long"
        return jsonify({'message': msg}), 400