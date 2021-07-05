import datetime
import json
import logging
import os

import azure.functions as func

from fpl.data.odds import get_odds


def main(mytimer: func.TimerRequest, outputblob: func.Out[bytes]) -> None:
    if mytimer.past_due:
        logging.info("The timer is past due!")
    api_key = os.getenv("ODDS_API_KEY")
    print("HERE")
    logging.info(api_key)
    odds = {}
    odds["h2h"] = get_odds(market="h2h", api_key=api_key)
    odds["over_under"] = get_odds(market="totals", api_key=api_key)

    outputblob.set(json.dumps(odds, ensure_ascii=False))
