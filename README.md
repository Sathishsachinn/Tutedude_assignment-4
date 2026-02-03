# Python File Handling Programs

This repository contains two Python programs that demonstrate basic file handling concepts such as reading files, writing data, appending content, and handling errors gracefully.

---

## Problem 1: Reading a File With Error Handling

### Description

This program attempts to open and read a text file named `sample.txt`.
If the file exists, it prints the content line by line.
If the file does not exist, it handles the error properly and displays a message.

### Features

* Uses `try-except` for error handling
* Reads file content line by line
* Prevents program crash if the file is missing

### Expected Output

**If the file exists:**

```
file consists of
line 1:this is a simple text file
line 2:consist multiple line
```

**If the file does not exist:**

```
file not found
```

### Key Concepts Used

* `open()` function
* `with` statement
* `FileNotFoundError` exception

---

## Problem 2: Writing, Appending, and Reading a File

### Description

This program takes user input and performs three operations on a file named `output.txt`:

1. Writes user input to the file
2. Appends additional data to the same file
3. Reads and displays the final content

The file is automatically created if it does not exist.

### Features

* Takes user input from the console
* Writes and appends text to a file
* Reads and displays file content

### Expected Output (Example)

```
Enter text to write to the file: Hello, Python!

Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.

Data successfully appended.

Final content of output.txt:

Hello, Python!
Learning file handling in Python.
```

### Key Concepts Used

* File modes: `w`, `a`, `r`
* Writing and appending data
* Reading full file content

---

## Requirements

* Python 3.x
* No external libraries required

---

## How to Run

1. Open a terminal or command prompt
2. Navigate to the project directory
3. Run the program using:

```
python filename.py
```


## Learning Outcomes

* Understanding file handling in Python
* Working with different file modes
* Handling file-related errors safely
* Reading and writing user input to files
