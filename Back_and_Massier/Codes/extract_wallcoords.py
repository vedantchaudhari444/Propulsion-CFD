#Extract the next number after zero in the following file
###
# Open and read the file
file_path = "y_values.txt"  # Update with your file path
with open(file_path, "r") as file:
    raw_text = file.read()

# Split the text into tokens based on whitespace
tokens = raw_text.split()

# List to store extracted numbers before each "0"
following_numbers = []

# Iterate through tokens and extract numbers before "0"
for i in range(len(tokens) - 1):
    if tokens[i] == "0":
        following_numbers.append(tokens[i - 1])

# Print the extracted list
print(following_numbers)
