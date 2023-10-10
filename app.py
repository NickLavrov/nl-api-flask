from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Ping(Resource):
    def get(self):
        return {'message': 'pong', 'api': 'flask'}

class Pong(Resource):
    def get(self):
        return {'message': 'ping', 'api': 'flask'}

api.add_resource(Ping, '/ping')
api.add_resource(Pong, '/pong')

if __name__ == '__main__':
    app.run(debug=True)
