# Casting Agency API
Casting Agency app allows to list actors and movies and assign actors to movies. 
Hosted on heroku

## Database Setup (on heroku)
Add Postgres add-on by running:
```bash
heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_heroku_application
```
Change the DATABASE_URL environment variable in the app settings to the link for the Postgres add-on

## Deploying on heroku

Clone github project and connect it in the heroku app settings. Then push git project by executing:

```bash
git push heroku master
```

## Run migrations

```bash
heroku run python manage.py db upgrade --app name_of_your_application
```

## Roles

- Casting Assistant
        - Can view actors and movies
- Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors or movies
- Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database

## Endpoints

#### GET '/movies'
```bash
{
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
            "title": "Test Test"
        },
        {
            "id": 2,
            "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
            "title": "Test Test"
        }
    ],
    "success": true
}
```

#### GET '/actors'
```bash
{
    "actors": [
        {
            "birth_date": "Mon, 11 Nov 1991 00:00:00 GMT",
            "gender": "M",
            "id": 1,
            "name": "Test Test"
        },
        {
            "birth_date": "Mon, 11 Nov 1991 00:00:00 GMT",
            "gender": "M",
            "id": 2,
            "name": "Test Test"
        }
    ],
    "success": true
}
```
#### POST '/movies'
Request body:
```bash
{
    "title": "Test Test",
    "release_date": "3/3/2020"
}
```
Response:
```bash
{
    "movie": [
        {
            "id": 4,
            "release_date": "Tue, 03 Mar 2020 00:00:00 GMT",
            "title": "Test Test"
        }
    ],
    "success": true
}
```
#### POST '/actors'
Request body:
```bash
{
    "name": "Test Test",
    "birth_date": "11/11/1991",
    "gender": "M"
}
```
Response:
```bash
{
    "actor": [
        {
            "birth_date": "Mon, 11 Nov 1991 00:00:00 GMT",
            "gender": "M",
            "id": 2,
            "name": "Test Test"
        }
    ],
    "success": true
}
```

#### PATCH '/movies/<id>'
Request body:
```bash
{
    "release_date": "4/4/2020"
}
```
Response:
```bash
{
    "movie": [
        {
            "id": 1,
            "release_date": "Sat, 04 Apr 2020 00:00:00 GMT",
            "title": "Test Test"
        }
    ],
    "success": true
}
```

#### PATCH '/actors/<id>'
Request body:
```bash
{
    "gender": "F"
}
```
Response:
```bash
{
    "actor": [
        {
            "birth_date": "Mon, 11 Nov 1991 00:00:00 GMT",
            "gender": "F",
            "id": 1,
            "name": "Test Test"
        }
    ],
    "success": true
}
```

#### DELETE '/movies/<id>'

```bash
{
    "movie": [
        {
            "id": 1,
            "release_date": "Sat, 04 Apr 2020 00:00:00 GMT",
            "title": "Test Test"
        }
    ],
    "success": true
}
```

#### DELETE '/actors/<id>'

```bash
{
    "actor": [
        {
            "birth_date": "Mon, 11 Nov 1991 00:00:00 GMT",
            "gender": "F",
            "id": 1,
            "name": "Test Test"
        }
    ],
    "success": true
}
```

## Testing

### Unit tests
To run the tests, run
```
python test_app.py
```

### RBAC Postman tests
Download a postman collection and run it.
Variable host is set to localhost for local testing. For testing the heroku app change to https://casting-agency102.herokuapp.com/