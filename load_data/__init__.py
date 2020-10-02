import logging
import json
import azure.functions as func
from random import randint
from fpl.data import transformations

def main(myblob: func.InputStream, outputDoc: func.Out[func.DocumentList]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    

    outdata = json.loads(myblob.read().decode('utf-8'))
    download_time = outdata["download_time"]
    gameweek = transformations.get_game_week(outdata)
    transformations.add_gw_and_download_time(outdata["elements"], download_time, gameweek)
    transformations.add_unique_id(outdata["elements"])
    outputDoc.set(func.DocumentList(outdata["elements"]))

    
    