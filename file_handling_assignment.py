# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("Here is a number: 42\n")
            file.write("And here's another string: Python is great!\n")
        print("File 'my_file.txt' created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating/writing to the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied when trying to read 'my_file.txt'.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending a new line to the file.\n")
            file.write("Here is another number: 100\n")
            file.write("Final line: Enjoy coding!\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied when trying to append to 'my_file.txt'.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show the appended content

if __name__ == "__main__":
    main()
