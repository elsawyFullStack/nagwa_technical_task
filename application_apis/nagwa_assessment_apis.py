"""
This file contains all the apis endpoints
"""
# import flask restful resource
from flask_restful import Resource, reqparse
from handle_excel import read, write

excel_file_path = '/home/elsawy/courses/BestHundredBooks.xlsx'
class BestBooks(Resource):
    def get(self):
        """
        the implementation of retrieve functionality the 'R' in CRUD
        :return: list of all books
        """
        try:
            books = read(excel_file_path)

            return {"message": "success",
                    "data": {'books': books}
                    }

        except:
            return {"message": "Exception Happened Please Check Your Args If any"
                               ", and check the format of your Request and its data! "}

        return {"message": "Something Unusual Happened Please Return to Admin!"}

    def post(self):
        """
        the implementation of create/add functionality the 'C' in CRUD
        """
        # this should get the request data and append to alist
        # the list should be of the same order the file columns

        # parse the request data
        parser = reqparse.RequestParser()
        parser.add_argument('sequence', type=int)   # الترتيب
        parser.add_argument('novel', type=str)      # الروايه
        parser.add_argument('author', type=str)     # المؤلف
        parser.add_argument('country', type=str)    # البلد
        parser.add_argument('link', type=str)       # الرابط

        # get the params
        book_sequence = parser.parse_args().get('sequence')
        book_name = parser.parse_args().get('novel')
        book_author = parser.parse_args().get('author')
        book_country = parser.parse_args().get('country')
        book_link = parser.parse_args().get('link', '')

        if book_sequence and book_name and book_author and book_country:
            write(excel_file_path, [book_sequence, book_name,book_author, book_country, book_link])
            return {"message": "Successfuly added {}".format("Add")}

        return {"message": "Error Happened Make Sure you sent all the params with the right type!"}

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

