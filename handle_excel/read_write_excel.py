import openpyxl
import excel2json

books_sheet = openpyxl.load_workbook('../BestHundredBooks.xlsx')


def read():
    return books_sheet['Sheet1']


def write():
    pass


def edit():
    pass
