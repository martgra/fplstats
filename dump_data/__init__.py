import io
import json
import logging
from io import StringIO

import azure.functions as func
import pandas as pd

from fpl.visualization.display import make_race_bar_data


def main(
    documents: func.DocumentList, inputBlob: func.InputStream, outputBlob: func.Out[str]
) -> str:
    if documents:
        logging.info("Document id: %s", documents[0]["id"])

    old_data = StringIO(inputBlob.read().decode("utf-8"))
    old_data = pd.read_csv(old_data)

    listed = [dict(i) for i in documents]
    new_data = pd.DataFrame(listed)[
        ["web_name", "player_id", "team", "download_time", "transfers_in", "transfers_out"]
    ]

    new_data["diff"] = new_data["transfers_in"] - new_data["transfers_out"]
    new_data = make_race_bar_data(
        new_data[["web_name", "download_time", "diff", "team", "player_id"]],
        columns="download_time",
        index=["web_name", "team", "player_id"],
    )

    old_data = old_data.merge(new_data, how="left", on=["player_id"])
    print(old_data.head())

    merged = io.StringIO()
    old_data.to_csv(merged)

    outputBlob.set(merged.getvalue())
