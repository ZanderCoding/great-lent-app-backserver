# import ephem
# from datetime import datetime, timedelta
# import calendar
# import claculateVernalEquinox as cvl


# def calculate_first_sunday_after_full_moon(vernal_equinox_date):
#     # Calculate the date of the first full moon after the vernal equinox
#     observer = ephem.Observer()
#     observer.lon = '34'  # Observer longitude (0 for the Greenwich meridian)
#     observer.lat = '-118'  # Observer latitude (0 for the equator)
#     next_full_moon = ephem.localtime(
#         ephem.next_full_moon(ephem.localtime(vernal_equinox_date)))

#     # Find the first Sunday after the full moon
#     days_until_sunday = (6 - next_full_moon.weekday()) % 7
#     first_sunday_after_full_moon = next_full_moon + \
#         timedelta(days=days_until_sunday)

#     return first_sunday_after_full_moon


# # Example: Calculate the first Sunday after the vernal equinox in 2024
# # Example date for the vernal equinox
# vernal_equinox_date = datetime(2024, 3, 20)
# year = cvl.vernal_equinox_date
# # vernal_equinox_date = cvl.vernal_equinox_date
# first_sunday_after_full_moon = calculate_first_sunday_after_full_moon(
#     vernal_equinox_date)
# print(f"First Sunday after the full moon after the vernal equinox: {
#       first_sunday_after_full_moon}")
# import ephem
# from datetime import datetime, timedelta


# def calculate_first_sunday_after_full_moon(vernal_equinox_date):
#     # Convert vernal_equinox_date to ephem.Date
#     vernal_equinox_ephem = ephem.Date(vernal_equinox_date)

#     # Calculate the date of the first full moon after the vernal equinox
#     observer = ephem.Observer()
#     observer.lon = '34'  # Observer longitude (0 for the Greenwich meridian)
#     observer.lat = '-118'  # Observer latitude (0 for the equator)

#     # Use ephem.Date instead of ephem.localtime
#     next_full_moon = ephem.next_full_moon(vernal_equinox_ephem)

#     # Convert the result to a datetime object
#     next_full_moon_datetime = datetime.fromtimestamp(next_full_moon)

#     # Find the first Sunday after the full moon
#     days_until_sunday = (6 - next_full_moon_datetime.weekday()) % 7
#     first_sunday_after_full_moon = next_full_moon_datetime + \
#         timedelta(days=days_until_sunday)

#     return first_sunday_after_full_moon


# # Example: Calculate the first Sunday after the vernal equinox in 2024
# # Example date for the vernal equinox
# # vernal_equinox_date = datetime(2024, 3, 20)
# # year = cvl.vernal_equinox_date
# vernal_equinox_date = cvl.vernal_equinox_date
# first_sunday_after_full_moon = calculate_first_sunday_after_full_moon(
#     vernal_equinox_date)
# formatted_result = first_sunday_after_full_moon.strftime('%m-%d-%Y')
# print(f"First Sunday after the full moon after the vernal equinox: {
#       formatted_result}")
# import ephem
# from datetime import datetime, timedelta


# def calculate_julian_pascha(year):
#     # Set observer parameters for Julian calendar
#     observer = ephem.Observer()
#     # Observer longitude (e.g., 0 for the Greenwich meridian)
#     observer.lon = '0'
#     observer.lat = '0'  # Observer latitude (e.g., 0 for the equator)

#     # Calculate Pascha using the Julian calendar
#     pascha_date_julian = ephem.localtime(
#         ephem.Easter(year, method=ephem.Easter.Julian))
#     # pascha_date_julian = ephem.localtime(ephem.next_spring_equinox(str(year)))

#     # Find the Sunday after Pascha
#     days_until_sunday = (6 - pascha_date_julian.weekday()) % 7
#     pascha_sunday = pascha_date_julian + timedelta(days=days_until_sunday)

#     return pascha_sunday


# # Example: Calculate Pascha in the year 2024 using the Julian calendar
# year = 2024
# julian_pascha_date = calculate_julian_pascha(year)

# # Format the result for display
# formatted_result = julian_pascha_date.strftime('%Y-%m-%d')
# print(f"Pascha (Easter) in the year {
#       year} based on the Julian calendar: {formatted_result}")
# import ephem
# from datetime import datetime, timedelta


# def calculate_julian_pascha(year):
#     # Set observer parameters for Julian calendar
#     observer = ephem.Observer()
#     # Observer longitude (e.g., 0 for the Greenwich meridian)
#     observer.lon = '0'
#     observer.lat = '0'  # Observer latitude (e.g., 0 for the equator)

#     # Find the date of the first full moon after the spring equinox
#     spring_equinox = ephem.localtime(ephem.next_spring_equinox(str(year)))
#     full_moon_after_equinox = ephem.localtime(
#         ephem.next_full_moon(spring_equinox))

#     # Find the Sunday after the full moon
#     days_until_sunday = (6 - full_moon_after_equinox.weekday()) % 7
#     pascha_date_julian = full_moon_after_equinox + \
#         timedelta(days=days_until_sunday)

#     return pascha_date_julian


# # Example: Calculate Pascha in the year 2024 using the Julian calendar
# year = 2023
# julian_pascha_date = calculate_julian_pascha(year)

# # Format the result for display
# formatted_result = julian_pascha_date.strftime('%Y-%m-%d')
# print(f"Pascha (Easter) in the year {
#       year} based on the Julian calendar: {formatted_result}")
import ephem
from datetime import datetime, timedelta


def calculate_julian_pascha(year):
    # Set observer parameters for Julian calendar
    observer = ephem.Observer()
    # Observer longitude (e.g., 0 for the Greenwich meridian)
    observer.lon = '0'
    observer.lat = '0'  # Observer latitude (e.g., 0 for the equator)

    # Find the date of the first full moon after March 21 in the Julian calendar
    march_21_julian = ephem.localtime(ephem.next_spring_equinox(str(year)))
    full_moon_after_march_21 = ephem.localtime(
        ephem.next_full_moon(march_21_julian))

    # Find the Sunday after the full moon
    days_until_sunday = (6 - full_moon_after_march_21.weekday()) % 7
    pascha_date_julian = full_moon_after_march_21 + \
        timedelta(days=days_until_sunday)

    return pascha_date_julian


# Example: Calculate Pascha in the year 2024 using the Julian calendar
year = 2024
julian_pascha_date = calculate_julian_pascha(year)

# Format the result for display
formatted_result = julian_pascha_date.strftime('%Y-%m-%d')
print(f"Pascha (Easter) in the year {
      year} based on the Julian calendar: {formatted_result}")
