import json
#descargar projects.json de https://www.artstation.com/users/emanuelsko/projects.json
with open("h:\\Temp\\projects.json",encoding='utf-8') as f:

    projects=json.load(f)

with open("h:\\Temp\\ur.txt","wt") as f2:
    for project in projects["data"]:
        f2.write(f'{project["permalink"]}\n')


pass