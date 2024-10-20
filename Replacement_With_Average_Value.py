import pandas as pd

# Load the CSV file
df = pd.read_csv("C:/Users/Mrunal/Downloads/MBA-IT/Semester 2/(FDS) Fundamentals of Data Science/Road.csv")

columns_to_replace = ['Age_band_of_driver', 'Service_year_of_vehicle']

# Iterate through each column and replace blank values with mean
for column in columns_to_replace:
    # Convert the column to numeric (errors='coerce' will convert non-numeric values to NaN)
    df[column] = pd.to_numeric(df[column], errors='coerce')
    # Calculate mean excluding NaN values
    mean_value = df[column].mean()
    # Replace NaN (blank) values with the mean
    df[column].fillna(mean_value, inplace=True)


df.to_csv("C:/Users/Mrunal/Downloads/MBA-IT/Semester 2/(FDS) Fundamentals of Data Science/Road.csv", index=False)