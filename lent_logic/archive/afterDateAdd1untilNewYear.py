from datetime import datetime, timedelta
import findingPaschaAndLent as jcp


def check_and_increment_year(current_date, pascha):
    if current_date.date() > pascha:
        # If the current date has passed the start of Passover, increment the year
        new_year = current_date.date().year + 1
        return new_year
    else:
        return current_date.date()


# Example: Check and increment year if needed
# current_date = datetime(2024, 5, 6)  # Replace with the current date
current_date = datetime.now()
pascha = jcp.pascha_date

year = check_and_increment_year(current_date, pascha)

# print(f"The adjusted year is: {year}")
