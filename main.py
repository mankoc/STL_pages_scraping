import cgtrader
from cults import scrape_cults
from artstation import scrape_artstation
URL = f"https://www.cgtrader.com/3d-print-models/miniatures/figurines/tekken-anna-williams-fan-art-statue-3d-printable-0e0ce76c-47e7-4dc0-9da1-4f3e67e2b4d0"

OUTPUT_DIR="h:\\temp\\"

if "cgtrader.com" in URL:
    cgtrader.scrape_cgtrader(URL,OUTPUT_DIR)
if "cults3d" in URL:
    URL=URL.replace("https://cults3d.com/es/modelo-3d/arte/","https://cults3d.com/en/3d-model/art/")
    scrape_cults(URL,OUTPUT_DIR)
if "artstation" in URL:
    scrape_artstation(URL, OUTPUT_DIR)