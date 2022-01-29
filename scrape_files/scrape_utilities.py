"""
Usage: Contains the Implementation to
       scraping utilities
"""
# firstly importing libraries needed
# to send http requests
import urllib.request
import requests
# beautiful soup (get data using html filters)
from bs4 import BeautifulSoup

# use this library to send data to a Google sheet
# using Google apis
import pygsheets


def url_get_contents(url):
    """
    Used to Get the Content of a website using its url
    :param url: the website url that you need to scrape data from
    :return: the website content
    """
    request = urllib.request.Request(url=url)

    # get the content(open the url)
    content = urllib.request.urlopen(request)

    # reading contents of the website
    return content.read()


def write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, content_dataframe):
    """
    this function takes data frame and writes it under spreadsheet_id
    and sheet_name using your credentials under service_file_path
    :param service_file_path   the key file from Google apis
    :param spreadsheet_id      the id of your sheet
    :param sheet_name          the sheet you will append data to
    :param content_dataframe   the dataframe to be exported
    """
    # connect to google sheet api
    try:
        google_connect = pygsheets.authorize(service_file=service_file_path)
    except:
        print("You Did Not Have Access To Google API, please make sure you have the "
              "authorization key and passing its path correctly")

    # spreadsheet in your project
    try:
        spreadsheet = google_connect.open_by_key(spreadsheet_id)
    except:
        print("Error Happened Make sure of the provided sheet id!")
    try:
        # add sheet if not existing otherwise overwrite it
        spreadsheet.add_worksheet(sheet_name)
    except:
        print("Something Wrong happened , Please make sure you provided the correct sheet name")
    # write to the sheet
    wks_write = spreadsheet.worksheet_by_title(sheet_name)
    wks_write.clear('A1', None, '*')
    wks_write.set_dataframe(content_dataframe, (1, 1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1
    print(f"Data Has Been Exported to your sheet: {sheet_name} \nwith id {spreadsheet_id}!")


# initialize the list with hte header that will be in the excel sheet
links = ['الرابط']


def get_urls(url):
    """
    used to Get the table links for only the names
    can be extended to get all the links if required
    :param url: the website url
    :return: list of links
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books_table = soup.find_all('table')[0]
    for row in books_table.find_all('tr'):
        for i in range(len(row.find_all('td'))):
            if i == 1:
                print(row.find_all('td')[i].find('a').attrs['href'])
                print('=======')
                links.append('https://ar.wikipedia.org' + row.find_all('td')[i].find('a').attrs['href'])

    return links