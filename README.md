# nagwa_technical_task
Assessment Task For Nagwa

##Usage: 
Perform all functionalities 
  ##### 1 - Prepare your Environment and install the requirements using 
      pip install -r requirements.txt
or whatever the way you get your required packages.

#### 2 - Scrape Data From The Wiki
    RUN: scrape.py
You will get two files BestHundredBooks.xlsx and Best100.csv

Data also will be saved to google sheet and make sure you have the access key and correctly set its path.

    e.g:
    for linux: /home/user/mydir/key_file.json
    for windows: C:\\users\\folder\\key_file.json

#### 3 - You Can use APIS to do CRUD operations on the Resulted Data from scraping
    Start your Server
    e.g RUN: flask run

#### 4 - To Create The Books Cover You should go to QRGenerator/create_book_covers and set the paths of the files and the place where you will save the books covers.


    RUN create_book_covers.py

You will Get Files under the path you will provide with each file name containing the QR for the book hyperlink
##Note:
            Python Version should be >= 7.x.x.x


**Make Sure To Have All the requirements and the key to Authenticate google Apis.**

As the code is Running you Can monitor the process through system logs.

You Can Control where to save the newly generated Files and by default it is saved where you are running your program.


# Parts
 ### Part 1
####Data scraping 
    RUN : scrape_files/scrape.py
Data is scraped and saved to a local **Excel** and **CSV** files
then sent to Google Sheet.

**_You Should have access key(json file to get authentication required to send data to Google apis)_**


 ### Part 2
#### Apis
    RUN: flask run

### Part 3     
#### PDF and QR Code Generator
the structure contains package for QR generator
which exports a PDF file containing the QR Code
to use separately you can .
###
    RUN: QRGenerator/create_pdf


This Part will be also imported while adding new books.
