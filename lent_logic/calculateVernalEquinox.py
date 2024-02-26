import ephem
from datetime import datetime


def calculate_vernal_equinox(year):
    observer = ephem.Observer()
    observer.lon = '34'  # Observer longitude (0 for the Greenwich meridian)
    observer.lat = '-118'  # Observer latitude (0 for the equator)

    equinox_date = ephem.localtime(ephem.next_vernal_equinox(str(year)))
    # print(observer)
    return equinox_date


# Example: Calculate vernal equinox for the year 2024
# current_date = datetime(2026, 1, 1)
current_date = datetime.now()
vernal_equinox_date = calculate_vernal_equinox(current_date).date()
print(f"Vernal Equinox on {current_date}: {vernal_equinox_date}")


# march 19 2024
# add 13 days to march 19
# equals april 1 2024
# next full moon is 23 april 2024
# next sunday is april 28 2024
# but is during jewish passover
# so is delayed unitl next week
# so pascha is on may 5 2024
