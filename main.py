#  creates a file in a specified directory, then asks user for input.
import os

def create_file_in_directory():
    directory = input("Enter the directory where you want to create the file: ")
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    file_name = input("Enter the name of the file to create: ")
    file_path = os.path.join(directory, file_name)

    file_content = input("Enter the data to write in the file: ")

    try:
        with open(file_path, 'w') as file:
            file.write(file_content)
        print(f"File '{file_name}' created successfully in '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_file_in_directory()
