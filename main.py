from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource, request
from solver import solver

app = Flask(__name__)
api = Api(app)



class ProductionPlan(Resource):
    def get(self):
        return TODOS

    def post(self):
        try:
            TODOS = request.get_json()
            return solver(TODOS), 201
        except Exception as e:
            return 'Error occurred : ' + str(e)


##
## Actually setup the Api resource routing here
##
api.add_resource(ProductionPlan, '/productionplan')

if __name__ == '__main__':
    app.run(debug=True,port=8888)
