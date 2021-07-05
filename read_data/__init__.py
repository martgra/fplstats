"""Read data from Cosmos db."""
import json
import logging

import azure.functions as func


def main(req: func.HttpRequest, inputDocument: func.DocumentList) -> func.HttpResponse:
    """Serverless function to trigger read from Cosmos DB."""
    # pylint: disable=E1136
    logging.info(f"Python HTTP trigger function processed a request {req.body}.")
    listed = [dict(i) for i in inputDocument]
    listed = bytes(json.dumps(listed, ensure_ascii=False).encode("utf-8"))
    return func.HttpResponse(
        body=listed, mimetype="application/json", headers={"Content-Length": str(len(listed))}
    )
