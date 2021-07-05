"""Scrape data from FPL API."""

import datetime
import json
import logging

import azure.functions as func
import requests


def main(mytimer: func.TimerRequest, outputblob: func.Out[bytes]):
    # pylint: disable=E1136
    """Serverless scraping function."""
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info("The timer is past due!")

    url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    fpl_json = requests.get(url).json()
    download_time = str(datetime.datetime.now())
    fpl_json["download_time"] = download_time

    logging.info("Python timer trigger function ran at %s", utc_timestamp)
    outputblob.set(json.dumps(fpl_json, ensure_ascii=False))
