"""
Usage: to scrape data and export it to csv file(excel sheet, CSV)
and append to google sheets
activate the env with the requirements
This File is run using : python3 scrape.py
                         or using the interpreter and 'run'

Dependency: scrape utilities
Files to have: the access key for the Google apis (.json) file
"""
import os
# import utility functions
from scrape_utilities import url_get_contents, write_to_gsheet, get_urls

# pretty-print python data structures
from pprint import pprint

# for parsing the table content
from html_table_parser.parser import HTMLTableParser

# convert data into data frame (rows and columns
import pandas as pd


# the url of the website
best_hundred_books = 'https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9'
# get Extensible HyperText Markup Language for the web page
xhtml = url_get_contents(best_hundred_books).decode('utf-8')

# Defining the HTMLTableParser object
parser = HTMLTableParser()

# feeding the html contents in the parser
parser.feed(xhtml)

# Now finally obtaining the data of the table
# ( we are obtaining the first and only existing table in the website
pprint(parser.tables[0])

# get the links from the table
links = get_urls(best_hundred_books)

# converting the parsed data to dataframe
content_dataframe = pd.DataFrame(parser.tables[0])

# add the links to the data frame of the table
content_dataframe[4] = links

# Show the data frame in the console
print(f"PANDAS DATAFRAME\n{content_dataframe}")

"""
 Export the data frame into Excel Sheet
 the file is saved in the current directory
 (the directory where you are running the script)
 if the file exists it will be overwritten
 otherwise it will be created
"""

# Create Excel Sheet
excel_file_name = 'BestHundredBooks.xlsx'
content_dataframe.to_excel(excel_file_name, index=False, header=False)


print(f"Scraped Data Has Been Exported to an Excel Sheet Named {excel_file_name} under the current working "
      f"Directory/Path{os.getcwd()}")

# Create CSV file
csv_file_name = 'Best100.csv'
content_dataframe.to_csv(csv_file_name, index=False, header=False)
print(f"Scraped Data Has Been Exported to an CSV File Named: {csv_file_name}\nunder the current working "
      f"Directory/Path: {os.getcwd()}")

# Google Sheets Part
# You Can Access the Sheet form Here
# https://docs.google.com/spreadsheets/d/14rLX8kp4i6ityBKEQ7YRy06v0ho8oPTKNMgG8xGkm2Y/edit?usp=sharing
# Spread Sheet Id between d/'id'/ in the sheet url
spreadsheet_id = '14rLX8kp4i6ityBKEQ7YRy06v0ho8oPTKNMgG8xGkm2Y'

# sheet name by default use the first sheet
# though you can use any other
sheet_name = "Sheet2"

# the auhenticator file
# the key you get from your api service
# I'm using the file name as it is located in the same dir
# you can pass your relative file path but it's advised to put the absolute one
service_file_path = 'nagwa-assesment-273b22c012ff.json'

# Call the utility of sending data to Google Sheet
write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, content_dataframe)
