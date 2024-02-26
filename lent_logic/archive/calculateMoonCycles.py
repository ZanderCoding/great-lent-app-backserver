import ephem


def calculate_moon_phase(date):
    moon = ephem.Moon(date)
    phase_description = ephem.phase(moon)
    return phase_description


# Example: Calculate moon phase for a specific date
date = '2024-01-14'
moon_phase = calculate_moon_phase(date)
print(f"Moon phase on {date}: {moon_phase}")
