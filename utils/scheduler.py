import pandas as pd
from datetime import datetime

def assign_drivers(shifts_df: pd.DataFrame, drivers_df: pd.DataFrame):
    """
    Simple round-robin assignment.
    Later we upgrade with:
    - 10 hour minimum/day
    - 27 days/month logic
    """

    if shifts_df.empty or drivers_df.empty:
        return pd.DataFrame()

    drivers = drivers_df.copy()
    drivers = drivers[drivers["active"].str.lower() == "active"]

    assignments = []
    driver_index = 0
    driver_list = drivers.to_dict("records")

    for _, shift in shifts_df.iterrows():
        required = int(shift.get("required_drivers", 1))

        for i in range(required):
            if not driver_list:
                continue

            driver = driver_list[driver_index % len(driver_list)]
            driver_index += 1

            assignments.append({
                "shift_id": shift["shift_id"],
                "date": shift["date"],
                "start_time": shift["start_time"],
                "end_time": shift["end_time"],
                "zone": shift["zone"],
                "driver_id": driver["driver_id"],
                "driver_name": driver.get("name_en", "")
            })

    return pd.DataFrame(assignments)
