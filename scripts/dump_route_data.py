import json
import xmltodict
import os
from pathlib import Path

def dump_route_numbers(path):
    route_numbers = []
    if not os.path.isdir("dumps"):
        os.mkdir("dumps")

    print("Extracting route numbers...")
    for child in Path(path).iterdir():
        if "shared_data" in str(child):
            continue
        child = str(child).rsplit("_", 2)[1]
        route_numbers.append(str(child))
               
    with open("dumps/route_numbers.json", "w", encoding='utf-8') as savefile:
        json.dump(route_numbers, savefile, indent=4, ensure_ascii=False)
    print(f"Route numbers dump is complete.\n")

def dump_route_names(path):
    route_names = []
    if not os.path.isdir("dumps"):
        os.mkdir("dumps")

    print("Extracting route names...")
    for child in Path(path).iterdir():
        if "shared_data" in str(child):
            continue
        with open(child, 'r', encoding='utf-8') as file:
            xml = file.read()
            route_info = xmltodict.parse(xml, encoding='utf-8')
            route_info = route_info["PublicationDelivery"]["dataObjects"]["CompositeFrame"]["frames"]["TimetableFrame"]["vehicleJourneys"]["ServiceJourney"]#.split("-", 9)
            for r in route_info:
                try:
                    name = r["Name"]
                    name = name.replace("–","-").replace(".", "")
                    if name not in route_names:
                        route_names.append(name)
                except:
                    pass # simply skip this one if unable to fetch name

    with open("dumps/route_names.json", "w", encoding='utf-8') as savefile:
        json.dump(route_names, savefile, indent=4, ensure_ascii=False)
    print("Route names dump is complete.\n")