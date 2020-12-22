import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, db, Movie, Actor, Role
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)

    @app.route('/')
    def index():
        return 'Hello!'

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.all()
            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies]
            })
        except Exception as e:
            print(e)
            abort(404)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.all()
            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in actors]
            })
        except Exception as e:
            print(e)
            abort(404)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        try:
            movie_json = request.get_json()
            movie = Movie(title=movie_json['title'], release_date=movie_json['release_date'])
            movie.insert()
            return jsonify({
                'success': True,
                'movie': [movie.format()]
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        try:
            actor_json = request.get_json()
            actor = Actor(name=actor_json['name'], birth_date=actor_json['birth_date'],
                          gender=actor_json['gender'])
            actor.insert()
            return jsonify({
                'success': True,
                'actor': [actor.format()]
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(payload, id):
        try:
            updated_movie = request.get_json()
            updated_title = updated_movie.get('title')
            updated_release_date = updated_movie.get('release_date')
            movie = Movie.query.filter_by(id=id).first()
            if movie:
                if updated_title:
                    movie.title = updated_title
                if updated_release_date:
                    movie.release_date = updated_release_date
                movie.update()
            else:
                print(id)
                abort(404)
            return jsonify({
                'success': True,
                'movie': [movie.format()]
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(payload, id):
        try:
            updated_actor = request.get_json()
            updated_name = updated_actor.get('name')
            updated_birth_date = updated_actor.get('birth_date')
            updated_gender = updated_actor.get('gender')
            actor = Actor.query.filter_by(id=id).first()
            if actor:
                if updated_name:
                    actor.name = updated_name
                if updated_birth_date:
                    actor.release_date = updated_birth_date
                if updated_gender:
                    actor.gender = updated_gender
                actor.update()
            else:
                print(id)
                abort(404)
            return jsonify({
                'success': True,
                'actor': [actor.format()]
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movie.query.filter_by(id=id).first_or_404()
            movie.delete()

            return jsonify({
                'success': True,
                'movie': [movie.format()]
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            actor = Actor.query.filter_by(id=id).first_or_404()
            actor.delete()

            return jsonify({
                'success': True,
                'actor': [actor.format()]
            })
        except Exception as e:
            print(e)
            abort(400)

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify(error.error), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
