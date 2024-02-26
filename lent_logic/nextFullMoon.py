import ephem
from datetime import datetime, timedelta
import lent_logic.calculateVernalEquinox as cve
import lent_logic.addRemoveDaysToDate as adtd


def find_next_full_moon(after_date):
    # Convert the given date to an ephem.Date object
    after_date_ephem = ephem.Date(after_date)

    # Find the date of the next full moon after the given date
    next_full_moon = ephem.localtime(ephem.next_full_moon(after_date_ephem))

    # Check if the next full moon is on the given date
    if next_full_moon.date() == after_date_ephem:
        return next_full_moon
    else:
        return after_date

# Example: Find the next full moon after a given date


# given_date_pascha = datetime(2026, 3, 20)  # Replace with your desired date
given_date_pascha = adtd.julian_vernal_equinox
next_full_moon_pascha = find_next_full_moon(given_date_pascha)

if next_full_moon_pascha:
    formatted_result = next_full_moon_pascha.strftime('%Y-%m-%d')
    print(f"The next full moon after {
          given_date_pascha} is on: {formatted_result}")
else:
    print(f"The full moon is on the given date: {given_date_pascha}")
