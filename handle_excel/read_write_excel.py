import openpyxl
import excel2json
import pandas as pd


def read(file_path, sheet='Sheet1'):
    """
    Reads all The content of a file(excel sheet)
    :param file_path: the path of the excel sheet
    :param sheet: the sheet name you want to get data from(default Sheet1)
    :return: content of the sheet as json
    """
    data_frame = pd.read_excel(file_path, sheet_name=sheet)
    return data_frame.to_json()


def write(file_path, data, sheet_name='Sheet1'):
    """
    used to append data to the file
    :param file_path: the file path
    :return:
    """
    books_sheet = openpyxl.load_workbook(file_path)
    sheet = books_sheet[sheet_name]
    sheet.append(data)
    books_sheet.save(file_path)


def edit(file_path, sequence):
    """
    To edit and update data in the sheet
    :param file_path: the file path
    :param sequence: the row sequence to be edited (الترتيب)
    :return:
    """
    # books_sheet = openpyxl.load_workbook(file_path)

def delete(file_path, sequence):
    """
    to delete from the excel sheet
    :param file_path:
    :param sequence:
    :return:
    """


write('/home/elsawy/courses/BestHundredBooks.xlsx', ['0', '0', '0', '0', '0', '0'])