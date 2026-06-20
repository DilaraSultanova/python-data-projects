import json

jobs = [
    {
        "title": "Software Engineering Intern",
        "company": "Tech Company",
        "location": "Remote"
    },
    {
        "title": "Python Developer",
        "company": "Startup Inc",
        "location": "New York"
    },
    {
        "title": "Backend Engineer",
        "company": "Data Systems",
        "location": "Remote"
    }
]

with open("jobs.json", "w") as file:
    json.dump(jobs, file, indent=4)

print("Job data saved successfully.")
