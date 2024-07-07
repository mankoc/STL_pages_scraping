import requests
from bs4 import BeautifulSoup
from utils import create_dir
import json
import os
from os import path as op
import urllib
from utils import clean_tags,write_url,clean_path
from pathvalidate import sanitize_filepath


# Press the green button in the gutter to run the script.
def scrape_stlflix(URL,OUTPUT_DIR):

    with open("config.json","rt") as f:
        config=json.load(f)


    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    images=soup.find_all("div", class_="thumb-list-wrapper js-list-wrapper")
    images = soup.find_all("jpg")
    main_dir = OUTPUT_DIR
