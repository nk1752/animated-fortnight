import os
import json
from datetime import datetime, timedelta


def load_dict(bg_name) -> dict:

    print("Loading dictionary...")
    print(f"BG_NAME: {bg_name}")
    # Load the dictionary from the file data.json
    with open("data.json", "r") as file:
        data = json.load(file)

        fgw_list = data["content"]

        fgw_dict: dict = {"dev_instances": [], "qa_instances": []}

        # Extract the keys from the dictionary
        for fwg_name in fgw_list:
            # get name
            name: str = fwg_name["name"]
            # get status from replicas
            status: str = fwg_name["status"]
            # get expiry
            if status == "CONNECTED":
                expiry = fwg_name["replicas"][0]["certificateExpirationDates"][0]
                count: int = fwg_name["replicas"][0]["count"]
                # if expiry not null then calculate time difference from now
                if expiry is not None:
                    # Parse the target timestamp into a datetime object
                    expiry_date: datetime = datetime.strptime(
                        expiry, "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                    # Get the current datetime
                    current_date: datetime = datetime.now()
                    diff: timedelta = expiry_date - current_date
                    days_to_expiry: int = diff.days
                else:
                    days_to_expiry = -9999

                fgw_dict["dev_instances"].append(
                    {
                        "fgw_name": name,
                        "status": status,
                        "count": count,
                        "expiry": expiry,
                        "days_to_expiry": days_to_expiry,
                    }
                )

        return fgw_dict
