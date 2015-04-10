from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# from app import views, models
from app.index import blueprint
from app.static.controllers import user

app.register_blueprint(blueprint)
app.register_blueprint(user)

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'Status': 404,
            'Error': 'Not Found ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
