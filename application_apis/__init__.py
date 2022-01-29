from .nagwa_assessment_apis import BestBooks

from flask_restful import Api

from app import flaskAppInstance

restServer = Api(flaskAppInstance)

restServer.add_resource(BestBooks, "/best_arabic_books")
