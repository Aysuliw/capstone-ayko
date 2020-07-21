# FSND Capstone Project: Casting Agency

This project is a summary of all the knowledge I gained in the Full Stack Nanodegree course.The Casting Agency is a company that is responsible for creating movies and managing and assigning actors to those movies.
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql capstone < capstone.psql
```

## Running the server

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app` directs flask to use  the `app.py` file to find the application. 

## Authentication : Roles, Permissions
- **Casting Assistant** - Permissons:
  - `get:movies`
  - `get:actors`
- **Casting Director** - All permissions a Casting Assistant has and ...
  - `post:actors`
  - `delete:actors`
  - `patch:movie`
  - `patch:actors`
- **Executive Producer** - All permissions a Casting Director has and ...
  - `post:movies`
  - `delete:movies`
## API Reference

### Error Handling

Errors are returned as JSON objects in the following fomrat:
```
{
  "error": 422,
  "message": "unprocessable",
  "success": false
}
```
The API will return 6 error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error

### Endpoints

GET '/actors'

- Returns a list of actors,success value

Sample : `curl -X GET -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:5000/actors`

```
 "actors": [
    {
      "age": 31,
      "gender": "Female",
      "id": 1,
      "name": "Emma Stone"
    },
    {
      "age": 61,
      "gender": "Male",
      "id": 2,
      "name": "Hugh Laurie"
    },
    {
      "age": 52,
      "gender": "Female",
      "id": 3,
      "name": "Julia Roberts"
    }
  ],
  "success": true
```
GET/movies
- Returns a list of actors,success value

Sample : `curl -X GET -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:5000/movies`
```
"movies": [
    {
      "id": 1,
      "release_date": "Tue, 16 Nov 2004 00:00:00 GMT",
      "title": "Dr. House"
    },
    {
      "id": 2,
      "release_date": "Wed, 31 Aug 2016 00:00:00 GMT",
      "title": "La La Land"
    },
    {
      "id": 3,
      "release_date": "Wed, 05 Dec 2001 00:00:00 GMT",
      "title": "Ocean's Eleven"
    }
  ],
  "success": true
```

POST/actors
- creates a new actor using the submitted name,age and gender. Returns the id of the created actor,success value and new actor details.

Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d'{"name":"name", "age": 27,"gender": "Male"}'`
```
  "actors": [
    {
      "age": 27,
      "gender": "Male",
      "id": 4,
      "name": "name"
    }
  ],
  "success": true
```
PATCH/movies/<id>
- update actor details with the given id and return id of the updated movie and success value.
Sample: `curl http://127.0.0.1:5000/movies/3 -X PATCH -H "Authorization: Bearer <ACCESS_TOKEN>" -H "Content-Type: application/json" -d'{"title":"The Hobbit: An Unexpected Journey","release_date": "2012-11-28"}'`
```
  "movies": [
    {
      "id": 3,
      "release_date": "Wed, 28 Nov 2012 00:00:00 GMT",
      "title": "The Hobbit: An Unexpected Journey"
    }
  ],
  "success": true
```
DELETE/actors/<id>
- Deletes actors with the given id and return id of the deleted actor and success value.

Sample: ` curl -X DELETE http://127.0.0.1:5000/actors/4 -H "Authorization: Bearer <ACCESS_TOKEN>"`
```
 "deleted": 4,
  "success": true
}
```

## Testing
To run the tests, run
```
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone.psql
python test_app.py
```