"""
This file contains all the apis endpoints
"""
# import flask restful resource
from flask_restful import Resource, reqparse


class BestBooks(Resource):
    def get(self):
        """
        the implementation of retrieve functionality the 'R' in CRUD
        :return: list of all books
        """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('sequence', type=int)
            book_sequence = parser.parse_args().get('sequence')
            if book_sequence:
                print(parser.parse_args())
                print(parser.parse_args().get('sequence'))
            books = ['1', '2', '3']

            return {"message": "success",
                    "data": {'books': books, 'extra': ''}
                    }

        except:
            return {"message": "Exception Happened Please Check Your Args If any"
                               ", and check the format of your Request and its data! "}

        return {"message": "Something Unusual Happened Please Return to Admin!"}

    def post(self):
        """
        the implementation of create/add functionality the 'C' in CRUD
        """
        return {"message": "Successfuly added {}".format("Add")}

    def put(self):
        """
        the implementation of updating/editing functionality the 'U' in CRUD
        """
        return {"message": "Successfuly Put "}


    def delete(self):
        """
        the implementation of deletion/removal functionality the 'D' in CRUD
        """
        return {"message": "Successfuly deleted"}

