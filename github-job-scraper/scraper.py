import requests
import json

url = "https://jobs.github.com/positions.json?description=python"

try:
    response = requests.get(url)
    jobs = response.json()

    with open("jobs.json", "w") as file:
        json.dump(jobs, file, indent=4)

    print(f"Saved {len(jobs)} jobs to jobs.json")

except Exception as e:
    print("Error:", e)
