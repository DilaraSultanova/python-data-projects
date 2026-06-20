resume_file = open("sample_files/sample_resume.txt", "r")
job_file = open("sample_files/job_description.txt", "r")

resume_text = resume_file.read().lower()
job_text = job_file.read().lower()

resume_words = set(resume_text.split())
job_words = set(job_text.split())

matching_skills = resume_words.intersection(job_words)
missing_skills = job_words.difference(resume_words)

match_score = round(
    (len(matching_skills) / len(job_words)) * 100, 2
)

print("AI RESUME ANALYZER")
print("-" * 30)

print(f"Match Score: {match_score}%")

print("\nMatching Keywords:")
for skill in sorted(matching_skills):
    print("-", skill)

print("\nMissing Keywords:")
for skill in sorted(missing_skills):
    print("-", skill)
