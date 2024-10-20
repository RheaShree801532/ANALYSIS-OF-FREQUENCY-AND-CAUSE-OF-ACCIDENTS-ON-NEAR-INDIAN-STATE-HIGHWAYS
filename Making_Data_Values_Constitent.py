import pandas as pd

# Load the dataset
file_path = "C:/Users/Mrunal/Downloads/MBA-IT/Semester 2/(FDS) Fundamentals of Data Science/Road.csv"
df = pd.read_csv(file_path)

# Replace blank values with "Unknown"
df['Service_year_of_vehicle'].replace("1-2yr", 1.5, inplace=True)
df['Service_year_of_vehicle'].replace("2-5yrs", 3.5, inplace=True)
df['Service_year_of_vehicle'].replace("5-10yrs", 7.5, inplace=True)
df['Service_year_of_vehicle'].replace("Above 10yr", 11, inplace=True)
df['Service_year_of_vehicle'].replace("Below 1yr", 0.5, inplace=True)

df.to_csv("C:/Users/Mrunal/Downloads/MBA-IT/Semester 2/(FDS) Fundamentals of Data Science/Road.csv", index=False)

print("Done.")