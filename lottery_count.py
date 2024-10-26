#first install pandas in order to open an excel file
#initially I thought since this opened in excel that I had to use pandas but after further
#review it's actually not needed but I left the code in there since I used column.mode

#open the file containing my csv file

#create a funtion to sort each column and find the most common number 

#run function 6 times, once for every colomn in the csv and store each return to a variable

#print each return in an array

import pandas as pd #creates alias for pandas

import numpy as np

filepath = 'C:/Users/Sean/Downloads/Mega_Millions_Numbers_2024.csv'

#loads a data frame using pandas
df = pd.read_csv(filepath) 

print("Column names:", df.columns.tolist())

#function to find the most common number in column
def most_common_number(column):
    return column.mode().iloc[0] if not column.mode().empty else None

#store the most common number
most_com_num = []

#points to specific columns to check
columns_of_interest = ['White Ball 1', 'White Ball 2', 'White Ball 3', 'White Ball 4', 'White Ball 5', 'Mega Ball']
 
#iterate through each column and find most common
for column in columns_of_interest:
    if column in df.columns:
        most_com_num.append(most_common_number(df[column]))
    else:
        print(f"column '{column}' not found in the dataframe.")

most_com_num = [int(num) for num in most_com_num]

print("most common numbers:", most_com_num)

fhand = open('C:/Users/Sean/Downloads/Mega_Millions_Numbers_2024.csv')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('C:/Users/Sean/Downloads/Mega_Millions_Numbers_2024.csv')
for line in fhand:
    line = line.rstrip()
    if line.startswith('3'):
        print(line)