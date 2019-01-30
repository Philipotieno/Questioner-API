""" function to perform validations"""
import re
from flask import jsonify
import datetime

now = datetime.datetime.now()


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
    #validate topic
    if validate_topic(data):
        return validate_topic(data)

    #validate date
    if validate_date(data):
        return validate_date(data)

    #validate location
    if validate_location(data):
        return validate_location(data)

def validate_questions(data):
    #validate title
    if validate_title(data):
        return validate_title(data)

    #validate title
    if validate_body(data):
        return validate_body(data)

def validate_firstname(data):
    """Validate firstname"""
    if not re.match(r'^[a-z]+$', data['firstname']):
        msg = "Firstname should have letters and should be 3 or more characters long with no space"
        return jsonify({'message': msg}), 400

def validate_lastname(data):
    """Validate firstname"""
    if not re.match(r'^[a-z]+$', data['lastname']):
        msg = "Lastname should have letters and should be 3 or more characters long with no space"
        return jsonify({'message': msg}), 400

def validate_username(data):
    """Validate username"""
    if not re.match(r'^[a-z0-9]{5,15}$', data['username']):
        msg = "Username should have letters or numbers or a combination of both and should be 5 or more characters long "
        return jsonify({'message': msg}), 400


def validate_email(data):
    """Validate email"""
    if not re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$', data['email']):
        msg = "Please input a valid email!"
        return jsonify({'message': msg}), 400

def validate_phone(data):
    """Validate phone_number"""
    if not re.match(r'^[07]\d{9}$', data['phone_number']):
        msg = "Please input a valid phone number of the format 0703473377!"
        return jsonify({'message': msg}), 400

def validate_password(data):
    """Validate password"""
    pswd = data['password']
    if len(pswd) < 8:
        msg = "Password should be at least 8 characters"
        return jsonify({'message': msg}), 400

    if re.search('[0-9]',pswd) is None:
        msg = "Make sure your password has a number in it"
        return jsonify({'message': msg}), 400

    if re.search('[a-z]',pswd) is None:
        msg = "Make sure your password has a lowercase letter in it"
        return jsonify({'message': msg}), 400

    if re.search('[A-Z]',pswd) is None:
        msg = "Make sure your password has an uppercase letter in it"
        return jsonify({'message': msg}), 400

    if re.search('[@#$%^&+=]',pswd) is None:
        msg = "Make sure your password has one special character @#$%^&+="
        return jsonify({'message': msg}), 400

def validate_topic(data):
    """Validate topic"""
    if not re.match(r'^[a-zA-Z0-9]{3,}$', data['topic']):
        msg = "Topic should have letters or numbers or a combination of both and should be 3 or more characters long"
        return jsonify({'message': msg}), 400

def validate_title(data):
    """Validate topic"""
    if len(data['title']) < 10:
        msg = "Length of the title should be 15 or more characters long"
        return jsonify({'message': msg}), 400

def validate_body(data):
    """Validate body"""
    if len(data['body']) < 25 :
        msg = "Length of the body should be 25 or more characters long"
        return jsonify({'message': msg}), 400

def validate_date(data):
    """Validate topic"""
    try:
        if datetime.datetime.strptime(data['happening_on'], '%d-%m-%Y'):
            pass
    except:
        msg = "Date should be in the format %DD-%MM-%YYYY"
        return jsonify({'message': msg}), 400

    if datetime.datetime.strptime(data['happening_on'], '%d-%m-%Y') < now:
        msg = "Date cannot be earlier than today"
        return jsonify({'message': msg}), 400

def validate_location(data):
    """Validate location"""
    if not re.match(r'^[a-z]{3,}$', data['location']):
        msg = "location letters or numbers or a combination of both and should be 3 or more characters long"
        return jsonify({'message': msg}), 400
