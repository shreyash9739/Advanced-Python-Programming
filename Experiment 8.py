# Open the input file
input_file = open("input.txt", "r")

# Read all the lines from the file
lines = input_file.readlines()

# Count the total number of lines
count = len(lines)

# Display the line count
print("Total number of lines:", count)

# Get the first two lines
first_two = lines[:2]

# Open a new file for writing
output_file = open("output.txt", "w")

# Write the first two lines into the new file
output_file.writelines(first_two)

# Close both files
input_file.close()
output_file.close()

print("First two lines have been written to output.txt")
