import database_functions
import url_functions
from user_interface import run_main_interface
import requests
from bs4 import BeautifulSoup

HEADER_FOR_GET_REQUEST = (
    {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                   "Safari/537.36",
     'Accept-Language': 'en-US, en;q=0.5'}
)



def main():
    '''Currently creates and clears all tables then runs user interface. **MUST CHANGE THIS DOCSTRING AS FUNCTION CHANGES**'''
    database_functions.create_all_tables()
    run_main_interface(True)

if __name__ == '__main__':
    main()