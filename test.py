import pandas as pd

file_path = r"C:\Users\Sean\Downloads\Mega_Millions_Numbers_2024.csv"

# Read the first few rows to check for headers
df_sample = pd.read_csv(file_path, nrows=5)
if df_sample.columns[0].isdigit():
    # No headers present, read the CSV without headers
    df = pd.read_csv(file_path, header=None)
else:
    # Headers are present
    df = pd.read_csv(file_path)

# Print the column names
print("Column names:", df.columns.tolist())


# Function to find the most common number in a column
def most_common_number(column):
    return column.mode().iloc[0] if not column.mode().empty else None

# List to store the most common number for each column
most_common_numbers = []

# Specify the six columns you are interested in
columns_of_interest = ['White Ball 1', 'White Ball 2', 'White Ball 3', 'White Ball 4', 'White Ball 5', 'Mega Ball']  # Replace with your actual column names

# Iterate through each specified column and find the most common number
for column in columns_of_interest:
    if column in df.columns:
        most_common_numbers.append(most_common_number(df[column]))
    else:
        print("Column '{column}' not found in the dataframe.")

most_common_numbers = [int(num) for num in most_common_numbers]

# Print the results as an array
print("Most common numbers:", most_common_numbers)