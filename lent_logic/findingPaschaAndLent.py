import lent_logic.findNextSunday as fns
import lent_logic.JewishPassoverDate as jpd
import lent_logic.addRemoveDaysToDate as adtd
from datetime import datetime


def pascha_compaired_to_jpass(pass_start_date, sunday_date, pass_end_date):
    if pass_start_date <= sunday_date <= pass_end_date:
        # date = sunday_date
        pascha = fns.find_next_sunday(pass_end_date)
        # pascha = adtd.add_days_to_date(date, 7)
        print(f'Pascha is on: {pascha}')
    elif pass_start_date > sunday_date:
        pascha = fns.find_next_sunday(pass_end_date)
        print(f'Pascha is on: {pascha}')
    else:
        pascha = sunday_date
        print(f'Pascha is on: {pascha}')
    return pascha


sunday_date = fns.next_sunday_date
pass_start_date = jpd.passover_start_date
pass_end_date = jpd.last_day_of_passover

# sunday_date = datetime(2026, 4, 5)
# pass_start_date = datetime(2026, 4, 2)
# pass_end_date = datetime(2026, 4, 8)

pascha_date = pascha_compaired_to_jpass(
    pass_start_date, sunday_date, pass_end_date)
# Great Lent
start_lent = adtd.remove_days_to_date(pascha_date, 48)
print(f'Great Lent starts on: {start_lent}')
