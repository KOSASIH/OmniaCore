from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class APIGateway:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_endpoint(self, endpoint, method, handler):
        api.add_resource(handler, endpoint)
        print(f"Created endpoint {endpoint} with method {method}")

    def run(self):
        app.run(host=self.host, port=self.port)

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}

class TerraformAPI(Resource):
    def post(self):
        data = request.get_json()
        # Process terraform data
        return {"message": "Terraform data processed successfully"}

class PlanetaryAPI(Resource):
    def get(self, planet_id):
        # Retrieve planetary data from database
        return {"planet_id": planet_id, "name": "Kepler-62f", "classification": "Terrestrial"}

api_gateway = APIGateway('localhost', 5000)
api_gateway.create_endpoint('/hello', 'GET', HelloWorld)
api_gateway.create_endpoint('/terraform', 'POST', TerraformAPI)
api_gateway.create_endpoint('/planets/<string:planet_id>', 'GET', PlanetaryAPI)
api_gateway.run()
