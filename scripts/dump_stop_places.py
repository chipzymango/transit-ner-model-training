import xml.etree.ElementTree as ET
import json
import os

def dump_stops(path):
    stop_places = []
    stop_places_found = 0
    if not os.path.isdir("dumps"):
        os.mkdir("dumps")
        
    namespaces = {
        'netex': "http://www.netex.org.uk/netex",
        'gml': "http://www.opengis.net/gml/3.2"
    }
    print("Extracting stop places...")

    if len(os.listdir(path)) <= 0:
        print(f"Could not find any stop places in: '{path}'")
    else:
        for file in os.listdir(path):
            file = os.path.join(path, file)
            tree = ET.parse(file)
            root = tree.getroot()
            for stop_place in root.findall('.//netex:StopPlace', namespaces):
                name = stop_place.find('netex:Name', namespaces).text
                lat = float(stop_place.find('netex:Centroid/netex:Location/netex:Latitude', namespaces).text)
                long = float(stop_place.find('netex:Centroid/netex:Location/netex:Longitude', namespaces).text)
                
                county = file.split("\\", 1)[1].split("_", 3)[1].split("-")[0]
                #stop_place_type = stop_place.find('netex:StopPlaceType', namespaces).text

                stop_places.append({
                    'name': name,
                    'lat': lat,
                    'long': long,
                    'county': county
                })
                stop_places_found += 1
        with open("dumps/stop_places.json", 'w+', encoding='utf-8') as savefile:
            json.dump(stop_places, savefile, indent=4, ensure_ascii=False)
        print(f"Stop place dump is complete. Found {stop_places_found} stops")