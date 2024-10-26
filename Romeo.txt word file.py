with open('C:/Users/Sean/Downloads/romeo.txt', 'r') as file:
    # Read the file line by line and split into words
    words = file.read().split()

# Convert all words to lowercase and remove duplicates by using a set
unique_words = set(word.lower() for word in words)

# Sort the unique words alphabetically
sorted_unique_words = sorted(unique_words)

# Display the sorted unique words
print("Unique words in the file:")
for word in sorted_unique_words:
    print(word)