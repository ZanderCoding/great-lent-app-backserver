from datetime import datetime, timedelta
import lent_logic.nextFullMoon as nfm


def find_next_sunday(after_date):
    # Find the date of the next Sunday after the given date
    days_until_sunday = (6 - after_date.weekday()) % 7
    next_sunday = after_date + timedelta(days=days_until_sunday)

    return next_sunday


# Example: Calculate the next Sunday after the full moon date
# full_moon_date = datetime(2024, 4, 1)  # Replace with your full moon date
full_moon_date = nfm.next_full_moon_pascha  # Replace with your full moon date
next_sunday_date = find_next_sunday(full_moon_date)

# Format the result for display
formatted_result = next_sunday_date.strftime('%Y-%m-%d')
print(f"The next Sunday after the full moon on {
      full_moon_date} is: {formatted_result}")
