from flask import Flask
import json
from flask import Flask, request, Response
import app
from users import UserRepo
from database import users as db_users
from matcher import Matcher


app = Flask(__name__)

userRepo = UserRepo(repo=db_users)


@app.route('/user', methods=["GET", "POST"])
def users():
    if request.method == 'GET':
        result = userRepo.getAll()
        return Response(json.dumps(result), mimetype='application/json', status=200)
    if request.method == 'POST':
        if not request.json:
            return Response(json.dumps({"error": "missing attributes"}), status=400)

        result = userRepo.create(
            name=request.json['name'], age=request.json['age'], sign=request.json['sign'])

        if int(request.json['age']) < 18:
            return Response(json.dumps({"error": "too young, too dumb to realize"}), status=403)

        if result is None:
            return Response(json.dumps({"error": "bad attributes"}), status=400)

        return Response(None, mimetype='application/json', status=201)


@app.route('/user/<int:id>', methods=["GET", "PUT", "DELETE"])
def user(id):
    if request.method == 'GET':
        result = userRepo.find(id)

        if result == None:
            return Response(json.dumps({"error": "user not found"}), status=404)

        return Response(json.dumps(result), mimetype='application/json', status=200)

    if request.method == 'PUT':
        if not request.json:
            return Response(json.dumps({"error": "missing attributes"}), status=400)

        if int(request.json['age']) < 18:
            return Response(json.dumps({"error": "too young, too dumb to realize"}), status=403)

        result = userRepo.update(id, name=request.json['name'], age=int(
            request.json['age']), sign=request.json['sign'])

        if result == None:
            return Response(json.dumps({"error": "user not found"}), status=404)
        return Response(json.dumps(result), mimetype='application/json', status=200)

    if request.method == 'DELETE':
        if not request.json:
            return Response(json.dumps({"error": "missing attributes"}), status=400)

        result = userRepo.delete(id)
        if result == None:
            return Response(json.dumps({"error": "user not found"}), status=404)

        return Response(json.dumps(result), mimetype='application/json', status=200)


@app.route('/match/<int:id>', methods=["GET"])
def match(id: int):
    user = userRepo.find(id)
    if user == None:
        return Response(json.dumps({"error": "user not found"}), status=404)
    result = Matcher().match(userRepo.getAll(), user)

    return Response(json.dumps(result), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run()
