# Open and read the file
import csv

file_path = "x_values.txt"  # Update with your file path
with open(file_path, "r") as file:
    raw_text = file.read()

# Split the text into tokens based on whitespace
tokens = raw_text.split()

# List to store extracted numbers after each "0"
#x_numbers = []

# Iterate through tokens and extract numbers after "0"
for i in range(0, (len(tokens) - 1), 50):
    x_coord = tokens[i];
    #if tokens[i] == "0":
        #following_numbers.append(tokens[i + 1])
    print(tokens[i])

# Print the extracted list
#Writing to csv file
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Index", "x_coord"])
    for i, val in enumerate(x_coord):
        writer.writerow([i + 1, val])
