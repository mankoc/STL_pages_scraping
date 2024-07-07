import FreeSimpleGUI as sg
from Scrapers import cgtrader
from Scrapers.cults import scrape_cults
from Scrapers.artstation import scrape_artstation,scrape_artstation_json
from Scrapers.myminifactory import scrape_myminifactory
from Scrapers.stlflix import scrape_stlflix
import json

# sg.theme('LightGrey3')   # Add a touch of color
# All the stuff inside your window.
with open("config.json", "rt") as f:
    config = json.load(f)


default_dir=config["default_dir"]
layout = [  [sg.Text('Url:'), sg.InputText()],
            [sg.Text(f'Output:'),sg.InputText(default_dir), sg.FolderBrowse("Change",initial_folder =default_dir)],
            [sg.Push(),sg.Button('Ok'), sg.Button('Cancel')] ,
            [sg.StatusBar("",key="statusbar")]]

# Create the Window
window = sg.Window('Download info', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    URL=values[0]
    OUTPUT_DIR=values["Change"]
    if len(OUTPUT_DIR)==0:
        OUTPUT_DIR=default_dir
    URL = URL.replace("\n", "")

    if "cgtrader.com" in URL:
        output= cgtrader.scrape_cgtrader(URL, OUTPUT_DIR)

    if "cults3d" in URL:
        URL = URL.replace("https://cults3d.com/es/modelo-3d/arte/", "https://cults3d.com/en/3d-model/art/")
        output=scrape_cults(URL, OUTPUT_DIR)
    if "artstation" in URL:
         json_resp=sg.popup_get_text("Copy url in browser and paste output json here",default_text=scrape_artstation(URL,OUTPUT_DIR))

         output = scrape_artstation_json(json_resp, OUTPUT_DIR)
         #sg.popup(f"Paste this url and put json {scrape_artstation(URL,OUTPUT_DIR)}")
#        output= scrape_artstation(URL, OUTPUT_DIR)
         pass
    if "myminifactory" in URL:
       output= scrape_myminifactory(URL,OUTPUT_DIR)
    if "stlflix" in URL:
        output=scrape_stlflix(URL,OUTPUT_DIR)
    if URL[0]=="{":

        pass
    outp=f"DONE"
    window['statusbar'].update(outp)
    window.refresh()
window.close()