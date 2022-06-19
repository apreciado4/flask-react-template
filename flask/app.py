from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from HelloApiHandler import HelloApiHandler

app = Flask(__name__)
CORS(app)  # comment this on deployment
api = Api(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


api.add_resource(HelloApiHandler, '/flask/hello')

if __name__ == '__main__':
    app.run()
