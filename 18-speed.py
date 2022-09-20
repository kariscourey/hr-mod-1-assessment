def average_trip_speed(trip):

    total_miles = 0
    total_hours = 0

    for leg in trip:
        total_miles += leg["miles"]
        total_hours += leg["hours"]

    try:
        return total_miles / total_hours

    except:
        return float("nan")
