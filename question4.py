# 1. Create and write
file = open("demo.txt", "w")
file.write("Hello, My Name Is Mahesh Jagtap\nThis is a Python file handling tutorial.\nHappy Coding!")
file.close()
print("File 'demo.txt' created and written successfully.")

# 2. Read all content
file = open("demo.txt", "r")
content = file.read()
print("--- File Content ---")
print(content)
file.close()

# 3. Read first 10 characters
file = open("demo.txt", "r")
partial_content = file.read(10)
print(f"First 10 characters: '{partial_content}'")
file.close()

# 4. Read the first line
file = open("demo.txt", "r")
first_line = file.readline()
print(f"First line: {first_line.strip()}") # strip() removes the newline char for clean printing
file.close()

# 5. Append text
file = open("demo.txt", "a")
file.write("\nThis line was appended later.")
file.close()
print("Text appended successfully.")

# 6. Check existence
import os

filename = "demo.txt"
if os.path.exists(filename):
    print(f"The file '{filename}' exists.")
else:
    print(f"The file '{filename}' does not exist.")

# 7. Create using 'x' mode
try:
    # Trying to create a new file named 'new_demo.txt'
    f = open("new_demo.txt", "x")
    f.write("This file was created exclusively.")
    f.close()
    print("File created successfully.")
except FileExistsError:
    print("Error: The file already exists.")


# 8. Using 'with' statement
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# 9. tell() and seek()
with open("demo.txt", "r") as file:
    print(f"Initial Position: {file.tell()}")
    print(f"Read 5 chars: {file.read(5)}")
    print(f"Position after reading: {file.tell()}")
    print("Resetting cursor to 0...")
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")
    print(f"Reading again from start: {file.read(5)}")

# 10. r+ mode (Read and Write)
with open("demo.txt", "r+") as file:
    content = file.read()
    print("Original:", content)
    
    file.seek(0)
    file.write("Hi!!!")
    print("File modified.")

# 11. a+ mode (Append and Read)
with open("demo.txt", "a+") as file:
    file.write("\nFinal Entry.")
    print(f"Cursor position: {file.tell()}")
    file.seek(0)
    content = file.read()
    print("--- Updated Content ---")
    print(content)