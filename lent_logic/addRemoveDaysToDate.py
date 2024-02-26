from datetime import datetime, timedelta
import lent_logic.calculateVernalEquinox as cve


def add_days_to_date(input_date, days_to_add):
    # Calculate the new date by adding the specified number of days
    new_date_add = input_date + timedelta(days=days_to_add)
    return new_date_add


def remove_days_to_date(input_date, days_to_add):
    # Calculate the new date by removing the specified number of days
    new_date_remove = input_date - timedelta(days=days_to_add)
    return new_date_remove


# input_date = datetime(2026, 3, 20)
input_date = cve.vernal_equinox_date
days_to_add = 13
julian_vernal_equinox = add_days_to_date(input_date, days_to_add)

print(f"The result after adding {
      days_to_add} days to {input_date} is: {julian_vernal_equinox}")
