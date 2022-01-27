"""
This file contains all the apis endpoints
"""
# import flask restful resource
from flask_restful import Resource
import logging as logger


class BestBooks(Resource):
    def get(self):
        """
        the implementation of retrieve functionality the 'R' in CRUD
        :return: list of all books
        """
        books = []
        return books

    def post(self):
        """
        the implementation of create/add functionality the 'C' in CRUD
        """
        pass

    def put(self):
        """
        the implementation of updating/editing functionality the 'U' in CRUD
        """
        pass

    def delete(self):
        """
        the implementation of deletion/removal functionality the 'D' in CRUD
        """
        pass

