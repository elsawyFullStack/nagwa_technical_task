from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.color.color import HexColor
from decimal import Decimal
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.table.flexible_column_width_table import FlexibleColumnWidthTable
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType
from borb.pdf.canvas.layout.layout_element import LayoutElement


def create_pdf(name, author , path=''):
    """
    used to create a PDF File for a book cover
    :param name: the Name of the file (Book Name)
    :param path: the place to save this file should end with /
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

    # Contact information
    layout.add(
        FlexibleColumnWidthTable(number_of_columns=2, number_of_rows=1)
        .add(
            Paragraph("Nagwa",
                      font_color=HexColor("#f92672"),
                      font_size=Decimal(50)
                      )
             )
        .add(
            Image(
                "https://contents.nagwa.com/content/images/nagwa-share.png",
                width=Decimal(128),
                height=Decimal(128),)
        )
            .no_borders()
    )


    # Code to generate a QR code LayoutElement
    qr_code: LayoutElement = Barcode(
        data="https://www.borbpdf.com",
        width=Decimal(150),
        height=Decimal(150),
        type=BarcodeType.QR,

    )

    layout.add(
        FlexibleColumnWidthTable(number_of_columns=2, number_of_rows=1)
            .add(qr_code)
            .add(
            Paragraph(
                """
                Book QR Code You Can 
                click or scan to 
                Go to the Book Page
                """,
                padding_top=Decimal(12),
                respect_newlines_in_text=True,
                font_color=HexColor("#666666"),
                font_size=Decimal(10),

            )
        )
            .no_borders()
    )

    page.append_remote_go_to_annotation(
        qr_code.get_bounding_box(), uri="https://www.borbpdf.com"
    )
    layout.add(
        Paragraph(
            name,
            font_color=HexColor("#228B22"),
            font_size=Decimal(50)
        )
    )

    layout.add(
        Paragraph(
            f'Author: {author}',
            font_color=HexColor("#4B0082"),
            font_size=Decimal(50)
        )
    )
    # Attempt to store PDF
    with open(path + name + ".pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)




create_pdf("klsks","Elsawy" , '/home/elsawy/Desktop/')