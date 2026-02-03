#task-1
# Python program to read a file and handle file not found error

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("file consists of")
        
        # Read and print the file line by line
        for line in file:
            print(line.strip())

except FileNotFoundError:
    # Handle the case when file does not exist
    print("file not found")


#task-2
# Python program for writing, appending, and reading a file

# Step 1: Take user input and write to the file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("\nData successfully written to output.txt.\n")

# Step 2: Take additional input and append to the same file
additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("\nData successfully appended.\n")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:\n")

with open("output.txt", "r") as file:
    print(file.read())


