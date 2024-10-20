import pandas as pd

# Load the dataset
file_path = "C:/Users/Mrunal/Downloads/MBA-IT/Semester 2/(FDS) Fundamentals of Data Science/Road.csv"
df = pd.read_csv(file_path)

# Define columns to check for blank values or "Unknown"
columns_to_check = ['Sex_of_driver', 'Driving_experience', 'Area_accident_occured']

# Filter out records with blank or "Unknown" values in specified columns
for column in columns_to_check:
    df = df[(df[column] != '') & (df[column] != 'Unknown')]

columns_to_check = ['Casualty_class', 'Sex_of_casualty', 'Age_band_of_casualty']

# Filter out records with blank or "Unknown" values in specified columns
for column in columns_to_check:
    df = df[(df[column] != 'na')]



df.to_csv("C:/Users/Mrunal/Downloads/MBA-IT/Semester 2/(FDS) Fundamentals of Data Science/Road.csv", index=False)

print("Done.")