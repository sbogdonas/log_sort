import pandas as pd
from collections import Counter

# Specify the file path to the CSV file containing security logs
filepath = 'C:/Users/Sean/Downloads/Security_Logs_2024.csv'

# Load the CSV data into a DataFrame using pandas
df = pd.read_csv("C:\\Users\\Sean\\Downloads\\CSV.txt")

print("Column names:", df.columns.tolist())  # Print available column names

# Function to find the most common entry in a given column
def most_common_entry(column):
    return column.mode().iloc[0] if not column.mode().empty else None

# List to store the most common entry from each specified column
most_common_entries = []

# Columns of interest (e.g., columns representing IPs or event types in a log file)
columns_of_interest = ['IP Address', 'Event Type', 'Username']  # Customize based on log data

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
