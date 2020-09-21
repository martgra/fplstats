import logging
import json
import azure.functions as func


def main(myblob: func.InputStream, outputDoc: func.Out[func.DocumentList]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    

    outdata = json.loads(myblob.read().decode('utf-8'))
    for i in outdata["elements"]:
        logging.info(type(i))
        i["datetime"] = str(outdata["download_time"])
        i["player_id"] = i["id"]
        del i["id"]
        
    outputDoc.set(func.DocumentList(outdata["elements"]))

    
    