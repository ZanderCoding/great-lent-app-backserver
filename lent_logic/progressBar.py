from tqdm import tqdm
from datetime import datetime, timedelta
import findingPaschaAndLent as fpal


def calculate_percentage(start_date, target_date):
    # Calculate the total days between start_date and target_date
    total_days = (target_date - start_date).days

    # Use tqdm to display the progress bar
    with tqdm(total=total_days, desc="Progress") as pbar:
        current_date = today
        while current_date < target_date:
            # Your processing logic goes here

            # Update the progress bar
            pbar.update(1)

            # Increment the current date
            current_date += timedelta(days=1)

    	 # Calculate the percentage
   	 percentage_done = ((target_date - current_date).days / total_days) * 100
    	 return percentage_done


# Example: Calculate the percentage from today to a target date
today = datetime(2024, 3, 19).date()
# today = datetime.now().date()
# start_date = datetime(2024, 1, 1).date()  # Replace with your start date
# target_date = datetime(2024, 12, 31).date()  # Replace with your target date
start_date = fpal.start_lent  # Replace with your start date
target_date = fpal.pascha_date  # Replace with your target date

percentage = calculate_percentage(start_date, target_date)
print(f"Percentage Done: {percentage:.0f}%")
