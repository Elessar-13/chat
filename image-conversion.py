import os
from ascii_magic import AsciiArt, from_image, from_url

def ask_user():
# Get directory and filename from user input
    directory = input("Enter the directory to save the image: ")
    filename = input("Enter the filename (including extension, e.g., example.png): ")
# Ensure the directory exists
    #if not os.path.exists(directory):
        #os.makedirs(directory)
# Combine the directory path and filename
    file_path = os.path.join(directory, f"{filename}.txt")
    try:
        image = from_image(filename)
        image.to_terminal(monochrome = True)
        image.to_file(path = file_path, monochrome = True)
    except:
        print("An error has occured.")  

def picture_conversion(): 
    end_program = False
    while not bool(end_program):
        choice = ''

        print(('\n') + "Select a choice: ")
        print("Option 1: Put in file")
        print("Option 2: End program")
        choice = input("Enter (1/2): ")

        if choice in ['1', '2']:
            match choice:
                case '1':
                    ask_user()
                case '2':
                    print("End program")
                    end_program= True
        else: 
            print(('\n') + "Invalid choice. Please enter a number between 1 and 2.")   

picture_conversion()
