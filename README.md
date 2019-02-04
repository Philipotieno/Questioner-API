[![Build Status](https://travis-ci.org/Philipotieno/Questioner-API.svg?branch=develop)](https://travis-ci.org/Philipotieno/Questioner-API) [![Coverage Status](https://coveralls.io/repos/github/Philipotieno/Questioner-API/badge.svg?branch=develop)](https://coveralls.io/github/Philipotieno/Questioner-API?branch=develop)[![Maintainability](https://api.codeclimate.com/v1/badges/b11644d544aed557b9d2/maintainability)](https://codeclimate.com/github/Philipotieno/Questioner-API/maintainability)

# Questioner
Questioner is a platform that allows users to crowdsource questions for a meetup

## Features
- Users can create an account.
- Signed up users can log into their account.
- Admin can create a meetup record.
- Users can get all upcoming meetup records.
- Users can get a specific meeetup record.
- Users can post a question to a specifc meetup
- Users can comment on a question.
- Users can upvote a question.
- Users can downvote a question.
- Users can RSVP a meetup.

## Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python microframework)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)

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
export SECRET_KEY="some random string"
export APP_SETTINGS="development"

export DB_URL="postgresql://localhost/questioner"
export DB_HOST="localhost"
export DB_NAME="database_name"
export TEST_DB="testdb"
export DB_USERNAME="user role"
export DB_PASSWORD="password"

source .env

python run.py


```
### Endpoints:
--------------

# Register user

`POST /api/v1/auth/users/register`

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

Required fields: `firstname`, `lastname`, `username`, `phone`, `email`, `password` Must be valid


# Login user

`POST /api/v2/users/login`

Example request body:

```source-json
{
    "username": "jakeake",
    "password": "jakejake"
}
```

Required fields: `email`, `password`

# Log in admin
`POST /api/v2/auth/login`
Example request body:

```source-json
{
    "username": "wiseadmin",
    "password": "jakejake"
}
```
# Create a meetup record

`POST /api/v2/meetups/<admin_id>`

Example request body:

```source-json
{
    "topic": "python meetup",
    "location": "loitoktok",
    "tags": "tagone, tag2 tagthree",
    "happening_on": "1-11-2019"
}
```

authentication required, returns a meetup

Required fields: `topic`, `location`, `tags`, `happening_on`

# Get all meetup records

`GET /api/v2/meetups/upcoming`

Example reSponse:

```source-json
{
    "meetups": {
        "1": {
            "id": "1",
            "happening-on": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
        },
         "2": {
            "id": "2",
            "happening_on": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
        },
        "3": {
            "id": "3",
            "happening_on": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
        },
    },
    "status": 200
}
```
No authentication required, returns a meetup

# Get specific meetup records

`GET /api/v2/meetups/<meetup_id>`

Example reSponse:

```source-json
{
    "meetups": {
        "1": {
            "id": "1",
            "happening_on": "1/11/2019",
            "location": "lolwe",
            "tags": "tagone, tag3",
            "topic": "Python"
    },
    "status": 200
}
```
authentication required, returns a meetup

Required: `<meetup_id>`

# Post a question to specific meetup

`POST /api/v1/questions/<int: meetup_id>`

Example request body:

```source-json
{
	"title":"why is python so popular",
	"body":"Lorem ipsum dolor sit amet,,
}
```

authentication required, returns a question

Required fields:   `title`, `body` 

# Upvote a question

`POST /api/v1/questions/<question_id>upvote`

Example request body:

```source-json
{
	"vote": "Upvote",
}
```

authentication required

Required fields: `vote`

# Downvote a question

`POST /api/v1/questions/<int:question_id>/downvote`

Example request body:

```source-json
{
	"vote": "Downvote"
}
```

authentication required

Required fields: `vote`

# RSVP a meetup

`POST /api/v1/meetup/<int:meetup_id>/rsvp`

Example request body:

```source-json
{
	"attending": "maybe"
}
```

authentication required

Required fields: `attending`