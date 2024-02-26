from pyluach import dates

import JewishPassoverDate as jpd
import calculateVernalEquinox as cve
import nextFullMoon as nfm
import findNextSunday as fns
import addRemoveDaysToDate as artd
import findingPaschaAndLent as fpal





def future_pascha(year):
    equinox = cve.calculate_vernal_equinox(year)
    print(f'equinox: {equinox}')
    to_julian = artd.add_days_to_date(equinox, 13)
    print(f'julian: {to_julian}')
    moon = nfm.find_next_full_moon(to_julian)
    print(f'moon: {moon}')
    next_sunday = fns.find_next_sunday(moon)
    print(f'next_sunday: {next_sunday}')
    heb_year = dates.GregorianDate(year, 1, 1).to_heb().year
    print(f'heb_year: {heb_year}')
    start_pass = jpd.calculate_passover_start_date(heb_year)
    print(f'start_pass: {start_pass}')
    end_pass = jpd.calculate_last_day_of_passover(start_pass)
    print(f'end_pass: {end_pass}')
    new_date = fpal.pascha_compaired_to_jpass(
        start_pass, next_sunday.date(), end_pass)
    print(f'new_date: {new_date}')
    return new_date


print(future_pascha(2026))