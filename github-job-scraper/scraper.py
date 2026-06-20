import requests
import json

URL = "https://remotive.com/api/remote-jobs?search=python"

try:
    response = requests.get(URL)
    data = response.json()

    jobs = []

    for job in data["jobs"][:10]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "location": job["candidate_required_location"],
            "url": job["url"]
        })

    with open("jobs.json", "w") as file:
        json.dump(jobs, file, indent=4)

    print(f"Saved {len(jobs)} jobs.")

except Exception as e:
    print("Error:", e)
