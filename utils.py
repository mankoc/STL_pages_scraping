import os
import re
from pathvalidate import sanitize_filepath
def create_dir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def clean_path(path):
    return sanitize_filepath(path.replace(":", "").replace("  ", " ").replace("/", "-"))
def clean_tags(input):
    cleaner=re.compile(('<.*?>'))
    output=re.sub(cleaner,"",input)
    return output

def write_url(main_dir,info):
    title=info["name"] + " - " + info["author"]

    title=title.replace("/","-")
    URL=info["url"]
    with open(sanitize_filepath(os.path.join(main_dir,f"{title}.url")),"wt") as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={URL}")

def clean_useless_names(name):
    a=["Fan Art", "Statue", "3d Printable",
       "3D print model",
       "model"]

    for replacement in a:
        pattern = re.compile(replacement, re.IGNORECASE)
        name=pattern.sub("", name)
    return name