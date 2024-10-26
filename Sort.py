import pandas as pd
from collections import Counter

# Specify the file path to the CSV file containing security logs
filepath = 'C:/Users/Sean/Downloads/CSV.txt'

# Load the CSV data into a DataFrame using pandas
try:
    df = pd.read_csv(filepath)
    print("Column names in the CSV file:", df.columns.tolist())  # Print available column names
except FileNotFoundError:
    print(f"File '{filepath}' not found. Please check the file path.")
    exit()

# Function to find the most common entry in a given column
def most_common_entry(column):
    return column.mode().iloc[0] if not column.mode().empty else None

# List to store the most common entry from each specified column
most_common_entries = []

# Columns of interest (adjusted based on actual column names)
columns_of_interest = ['IP_Address', 'Username', 'Status']

# Find the most common entry in each specified column
for column in columns_of_interest:
    if column in df.columns:
        most_common_entries.append((column, most_common_entry(df[column])))
    else:
        print(f"Column '{column}' not found in the DataFrame.")

# Print the most common entry for each column of interest
print("Most common entries per column:")
for column, entry in most_common_entries:
    print(f"{column}: {entry}")

# Count the total lines (rows) in the CSV file
line_count = len(df)
print(f"Total number of log entries (lines): {line_count}")

# Open the file to find lines starting with a specific character or string
specific_start = '3'  # Customize based on your specific pattern
print(f"\nLog entries starting with '{specific_start}':")

with open(filepath, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        if line.startswith(specific_start):
            print(line)
