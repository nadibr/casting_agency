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


#### GET '/actors'


#### POST '/movies'


#### POST '/actors'


#### PATCH '/movies/<id>'


#### PATCH '/actors/<id>'


#### DELETE '/movies/<id>'


#### DELETE '/actors/<id>'


## Testing

### Unit tests
To run the tests, run
```
python test_app.py
```

### RBAC Postman tests
Download a postman collection and run it