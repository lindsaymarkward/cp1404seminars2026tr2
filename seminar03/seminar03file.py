"""
Seminar 03 - Warmup Question
Write a program to read a file and print ONLY the lines that start with a #
The user should enter the filename.
"""

# Ask the user for the filename
filename = input("Enter filename: ")
try:
    with open(filename, "r") as in_file:
        for line in in_file:
            if line.startswith("#"):
                print(line.strip())
except FileNotFoundError as error:
    print(f"Error! {error}")

# Finished now (not a good comment)
