# UPG 5d

import os

# Function to list the files and folders in the current working directory.
def list_directory():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    for file in files:
        print(file)

# Function to move to another directory or print an error in case the directory is not found.
def change_directory(new_directory):
    try:
        os.chdir(new_directory)
    except FileNotFoundError:
        print("Directory not found", "\n")
    except NotADirectoryError:
        print(new_directory, "is not a directory", "\n")

# Function to print out the directory in which the user is currently standing.
def print_working_directory():
    current_directory = os.getcwd()
    print(current_directory)

# Function to print out the contents of a file of choice in the current working directory or print an error in case the file is not found.
def print_file_content(file_name):
    try:
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                print(content)
        else:
            print(file_name, "is not a file", "\n")
    except FileNotFoundError:
        print("File not found", "\n")


# Main loop
def main():
    while True:
        user_input = input("Write any of these commands (ls | pwd | cd | cat):  ")

        # Error handling and function calls
        command_tokens = user_input.split()

        # If there are no command tokens, restart the loop.
        if not command_tokens:
            continue

        # Assigns the command variable the first word in the user_input. Ex: cat <file>, cat is command_token[0].
        command = command_tokens[0]

        # Prints out the files and folders in the current directory.
        if command == 'ls':
            print()
            list_directory()
            print()

        # Changes the directory or prints how to use the command if the user only writes cd.
        elif command == 'cd':
            if len(command_tokens) < 2:
                print()
                print("Usage: cd <directory>")
                print()
            else:
                new_directory = command_tokens[1]
                print()
                change_directory(new_directory)
                print()

        # Prints out the current working directory path. Ex: /home/username/documents.
        elif command == 'pwd':
            print()
            print_working_directory()
            print()

        # Prints out the contents of a file or prints how to use the command if the user input is only cat.
        elif command == 'cat':
            if len(command_tokens) < 2:
                print()
                print("Usage: cat <file>")
                print()
            else:
                file_name = command_tokens[1]
                print()
                print_file_content(file_name)
                print()

        # Print out "Unknown command and the command that was input". Ex: Unknown command: touch.
        else:
            print()
            print("Unknown command:", command)
            print()

# If the file is run as a program start the main function.
if __name__ == "__main__":
    main()
