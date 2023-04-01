import os
import random
import subprocess
from datetime import datetime, timedelta

# Define repository path
repo_path = "."  # If you are running this script inside the repo folder

# Define the start and end dates
start_date = datetime(2023, 4, 1)
end_date = datetime.now()

# Probability of making a commit (adjust this to get ~80% green boxes)
commit_probability = 0.8

# Function to execute git commands
def run_command(command):
    subprocess.call(command, shell=True)

# Change to the specified repository path
os.chdir(repo_path)

# Create a file to track changes
filename = "contribution_tracker.txt"

# Loop through each date from start to end
current_date = start_date
while current_date <= end_date:
    # Decide randomly whether to make a commit on this day
    if random.random() < commit_probability:
        # Make a change to the file
        with open(filename, "a") as file:
            file.write(f"Commit on {current_date.strftime('%Y-%m-%d')}\n")

        # Stage the file, commit, and backdate the commit
        run_command("git add .")
        commit_message = f"Commit on {current_date.strftime('%Y-%m-%d')}"
        run_command(f'git commit -m "{commit_message}" --date="{current_date.strftime("%Y-%m-%dT12:00:00")}"')

    # Move to the next day
    current_date += timedelta(days=1)

# Push all commits at the end
run_command("git push origin main")
