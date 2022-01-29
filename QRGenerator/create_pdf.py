from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.pdf import PDF


def create_pdf(name, path='', qr=None):
    """
    used to create a PDF File for a book cover
    :param name: the Name of the file (Book Name)
    :param path: the place to save this file should end with /
    :param qr: the QR code of the Book complete absolute or relative path
    :return: PDF File with the given name under the given Path containing the given QR
    """
    # Create empty Document
    pdf = Document()

    # Create empty Page
    page = Page()

    # Add Page to Document
    pdf.append_page(page)

    # Create PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # Future content-rendering-code to be inserted here

    # Attempt to store PDF
    with open(path + name + ".pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


create_pdf('myG', '/home/elsawy/Desktop/')
