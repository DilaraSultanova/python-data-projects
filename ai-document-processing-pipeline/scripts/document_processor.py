import pandas as pd

df = pd.read_csv("sample_extracted_data.csv")

completed = df[df["Completion_Status"] == "Complete"]

print("Total Documents:", len(df))
print("Completed Documents:", len(completed))
