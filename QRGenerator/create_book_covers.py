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
        print('index:', index)
        print(row[1])
        try:
            create_pdf(filename=row[1], filepath=to_path, bookname='Book Name , sorry for not supporting arabic',
                       author='Author Name', qrurl='https://github')

        except:
            print("Probl")
            pass

generate_book_cover(from_file='/home/elsawy/courses/BestHundredBooks.xlsx', sheet='Sheet1', to_path='/home/elsawy/courses/')