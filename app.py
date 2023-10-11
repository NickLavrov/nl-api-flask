from datetime import datetime
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

class Time(Resource):
    def get(self):
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'timestamp': current_timestamp}

api.add_resource(Ping, '/ping')
api.add_resource(Pong, '/pong')
api.add_resource(Time, '/time')

if __name__ == '__main__':
    app.run(debug=True)
