import re

with open("sample_files/sample_resume.txt", "r") as resume_file:
    resume_text = resume_file.read().lower()

with open("sample_files/job_description.txt", "r") as job_file:
    job_text = job_file.read().lower()

resume_words = set(re.findall(r"\w+", resume_text))
job_words = set(re.findall(r"\w+", job_text))

matching_skills = resume_words.intersection(job_words)
missing_skills = job_words.difference(resume_words)

match_score = round(
    (len(matching_skills) / len(job_words)) * 100, 2
)

print("=" * 40)
print("AI RESUME ANALYZER")
print("=" * 40)

print(f"\nMatch Score: {match_score}%")

print("\nMatching Keywords:")
for skill in sorted(matching_skills):
    print(f"✓ {skill}")

print("\nMissing Keywords:")
for skill in sorted(missing_skills):
    print(f"✗ {skill}")

print("\nAnalysis Complete")
