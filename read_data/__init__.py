import logging

import azure.functions as func
import json


def main(req: func.HttpRequest, inputDocument: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    listed = [dict(i) for i in inputDocument]
    listed = bytes(json.dumps(listed, ensure_ascii=False).encode("utf-8"))
    return func.HttpResponse(body=listed, mimetype="application/json", headers={"Content-Length": str(len(listed))})
    
