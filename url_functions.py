import requests
from bs4 import BeautifulSoup

base_link = 'https://www.amazon.com'

def create_headphones_link(page_num):
    '''Creates headphone link with desired page number'''
    #If page number is 0, make 1 if it is then continue building string
    if page_num == 0:
        page_num = 1
    #If page number less than 0, make positive then continue building string
    elif page_num < 0:
        page_num = abs(page_num)
    headphones_link = f'{base_link}/s?k=over+ear+headphones&page={page_num}'
    return headphones_link

def create_microphone_link(page_num):
    '''Creates microphone link with desired page number'''
    #If page number is 0, make 1 if it is then continue building string
    if page_num == 0:
        page_num = 1
    #If page number less than 0, make positive then continue building string
    elif page_num < 0:
        page_num = abs(page_num)
    microphone_link = f'{base_link}/s?k=USB+microphone&page={page_num}'
    return microphone_link

def create_webcam_link(page_num):
    '''Creates webcam link with desired page number'''
    #If page number is 0, make 1 if it is then continue building string
    if page_num == 0:
        page_num = 1
    #If page number less than 0, make positive then continue building string
    elif page_num < 0:
        page_num = abs(page_num)
    webcam_link = f'{base_link}/s?k=1080p+webcam&page={page_num}'
    return webcam_link

def create_capture_card_link(page_num):
    '''Creates capture card link with desired page number'''
    #If page number is 0, make 1 if it is then continue building string
    if page_num == 0:
        page_num = 1
    #If page number less than 0, make positive then continue building string
    elif page_num < 0:
        page_num = abs(page_num)
    capture_card_link = f'{base_link}/s?k=capture+card&page={page_num}'
    return capture_card_link

def create_audio_mixer_link(page_num):
    '''Creates audio mixer link with desired page number'''
    #If page number is 0, make 1 if it is then continue building string
    if page_num == 0:
        page_num = 1
    #If page number less than 0, make positive then continue building string
    elif page_num < 0:
        page_num = abs(page_num)
    audio_mixer_link = f'{base_link}/s?k=8-channel+audio+mixer&page={page_num}'
    return audio_mixer_link

def create_gaming_laptop_link(page_num):
    '''Creates gaming laptop link with desired page number'''
    #If page number is 0, make 1 if it is then continue building string
    if page_num == 0:
        page_num = 1
    #If page number less than 0, make positive then continue building string
    elif page_num < 0:
        page_num = abs(page_num)
    laptop_link = f'{base_link}/s?k=gaming+laptop&page={page_num}'
    return laptop_link