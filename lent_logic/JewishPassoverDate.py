from datetime import datetime, timedelta
from pyluach import dates


def calculate_passover_start_date(year):
    # Calculate the date of the 15th day of Nisan
    nisan_15_date = dates.HebrewDate(year, 1, 15).to_pydate()
    return nisan_15_date


def calculate_last_day_of_passover(passover_start_date):
    # add 6 days to the start date for the end
    passover_last_day = passover_start_date + timedelta(days=6)
    return passover_last_day


# for calculate_passover_start_date
current_hebrew_year = dates.HebrewDate.today().year
jew_passover_start_date = calculate_passover_start_date(current_hebrew_year)


# for calculate_last_day_of_passover
passover_start_date = jew_passover_start_date
last_day_of_passover = calculate_last_day_of_passover(passover_start_date)


# check if current date is after passover
# current_gregorian_date = datetime(2026, 1, 1).date()
current_gregorian_date = datetime.now().date()
while current_gregorian_date > last_day_of_passover:
    current_hebrew_year += 1
    jew_passover_start_date = calculate_passover_start_date(
        current_hebrew_year)
    last_day_of_passover = calculate_last_day_of_passover(
        jew_passover_start_date)

formatted_result = jew_passover_start_date.isoformat()
print(f"The 15th day of Nisan in the year {
      current_hebrew_year} is: {formatted_result}")
formatted_result = last_day_of_passover.strftime('%Y-%m-%d')
print(f"The last day of Jewish Passover is: {formatted_result}")
