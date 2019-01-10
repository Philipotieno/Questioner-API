[![Build Status](https://travis-ci.org/Philipotieno/Questioner-API.svg?branch=develop)](https://travis-ci.org/Philipotieno/Questioner-API) [![Coverage Status](https://coveralls.io/repos/github/Philipotieno/Questioner-API/badge.svg?branch=develop)](https://coveralls.io/github/Philipotieno/Questioner-API?branch=develop)[![Maintainability](https://api.codeclimate.com/v1/badges/b11644d544aed557b9d2/maintainability)](https://codeclimate.com/github/Philipotieno/Questioner-API/maintainability)

# Questioner
Questioner is a platform that allows users to crowdsource questions for a meetup

## Features
- Users can create an account.
- Signed up users can log into their account.
- Users can create a meetup record.
- Users can get all upcoming meetup records.
- Users can get a specific meeetup record.
- Users can post a question to a specifc meetup
- Users can upvote a question.
- Users can downvote a question.
- Users can RSVP a meetup.

## Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python microframework)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)

## Getting started
**You can view the app on heroku at [https://maswala.herokuapp.com/](https://maswala.herokuapp.com/) and test the end points on postman**


### Endpoints:
--------------

# Register user

`POST /api/v1/users/register`

Example request body:

```source-json
{
    "firstname": "philip",
    "lastname": "otieno",
    "username": "otiphil",
    "phone": "0703473377",
    "email": "jake@jake.jake",
    "password": "jakejake"
}
```

No authentication required, returns a User

Required fields: `firstname`, `lastname`, `username`, `phone`, `email`, `password`


# Login user

`POST /api/v1/users/login`

Example request body:

```source-json
{
    "email": "jake@jake.jake",
    "password": "jakejake"
}
```

No authentication required, returns a User

Required fields: `email`, `password`


# Create a meetup record

`POST /api/v1/meetups`

Example request body:

```source-json
{
    "topic": "python meetup",
    "location": "loitoktok",
    "tags": "tagone, tag2 tagthree",
    "happeningOn": "1/11/2019"
}
```

No authentication required, returns a User

Required fields: `topic`, `location`, `tags`, `happeningOn`

# Get all meetup records

`GET /api/v1/meetups/upcoming`

Example reSponse:

```source-json
{
    "meetups": {
        "1": {
            "id": "1",
            "happeningOn": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
        },
         "2": {
            "id": "2",
            "happeningOn": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
        },
        "3": {
            "id": "3",
            "happeningOn": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
        },
    },
    "status": 200
}
```
No authentication required, returns a User

# Get specific meetup records

`GET /api/v1/meetups/<meetup_id>`

Example reSponse:

```source-json
{
    "meetups": {
        "1": {
            "id": "1",
            "happeningOn": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
    },
    "status": 200
}
```
No authentication required, returns a User

Required: `<meetup_id>`

# Post a question to specific meetup

`POST /api/v1/questions`

Example request body:

```source-json
{
	"User": 1,
	"meetup": 1,
	"title":"why is python so popular",
	"body":"Lorem ipsum dolor sit amet,,
}
```

No authentication required, returns a User

Required fields: `user`, `meetup`, `title`, `body` 

# Upvote a question

`POST /api/v1/questions/<question_id>upvote`

Example request body:

```source-json
{
	"User": 1,
	"upvote": 1,
}
```

No authentication required, returns a User

Required fields: `user_id`, `upvote`

# Downvote a question

`POST /api/v1/questions/<questio_id>/downvote`

Example request body:

```source-json
{
	"User": 1,
	"upvote": 1,
}
```

No authentication required, returns a User

Required fields: `user`, `downvote`

# RSVP a meetup

`POST /api/v1/meetup/<meetup_id>/rsvp`

Example request body:

```source-json
{
	"attending": "yes/no/maybe"
}
```

No authentication required, returns a User

Required fields: `attending`



## Setting up the application
```
 git https://github.com/Philipotieno/Questioner-API.git

 cd Questioner-API

 git checkout develop

 pip install virtualenv

 virtualenv -p python3 -name of virtualenv-

 source ./bin/activate

 pip install -r requirements.txt

 touch .env
 		Add the following
 			export FLASK_APP="run.py"
			export FLASK_ENV=development
			export SECRET="some random string

source .env

python run.py

pytest

```