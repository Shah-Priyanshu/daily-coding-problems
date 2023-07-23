import os
import re
from datetime import datetime, timedelta

def get_last_problem_and_date():
    # Get a list of all .py files in the current directory
    files = [file for file in os.listdir() if file.endswith(".py")]

    # Find the most recently created file based on the file's name
    if files:
        files.sort(reverse=True)
        last_file = files[1]
        match = re.search(r"Problem#(\d+)_(\d{4}-\d{2}-\d{2})", last_file)
        if match:
            last_problem_number = int(match.group(1))
            last_date_str = match.group(2)
            last_date = datetime.strptime(last_date_str, "%Y-%d-%m").date()
            return last_problem_number, last_date

    # If no .py files are found or no valid pattern is found in the filenames
    # return default values for problem number and date
    return 0, datetime.strptime("2023-21-07", "%Y-%d-%m").date()  # Default problem number and date

def increment_date(current_date):
    # Increment the date by one day
    return current_date + timedelta(days=1)

def create_python_file(filename):
    with open(filename, "w") as file:
        pass  # Empty file

if __name__ == "__main__":
    # Get the last problem number and date from the existing files
    last_problem_number, last_date = get_last_problem_and_date()

    # Increment the problem number for the new file
    problem_number = last_problem_number + 1

    # Increment the date for the new file
    new_date = increment_date(last_date)

    # Construct the filename using the given naming convention
    filename = f"Problem#{problem_number}_{new_date.strftime('%Y-%d-%m')}.py"

    # Check if the file already exists, if not, create it
    if not os.path.exists(filename):
        create_python_file(filename)
        print(f"File '{filename}' has been created.")
    else:
        print(f"File '{filename}' already exists.")
