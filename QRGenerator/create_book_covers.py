# import qrcode
#
# img = qrcode.make("https://github.com/elsawyFullStack")
#
# img.save('mygithub.jpg')

from create_pdf import create_pdf
import pandas as pd


def generate_book_cover(from_file, sheet, to_path=''):
    data_frame = pd.read_excel(from_file, sheet_name=sheet)
    data_frame = data_frame.reset_index()

    for index, row in data_frame.iterrows():
            try:
                create_pdf(filename=row[2], filepath=to_path, bookname='Book Name , sorry for not supporting arabic',
                           author='Author Name', qrurl=row[5])

            except Exception as e:
                print("Probl", e)
                pass

generate_book_cover(from_file='/home/elsawy/courses/nagwa_technical_task/scraping_output/BestHundredBooks.xlsx', sheet='Sheet1', to_path='/home/elsawy/courses/nagwa_technical_task/book_vovers/')