import os

# Define file extensions and their corresponding destination folders
extensions = {
    'Images': [
        '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp',
        '.svg', '.raw', '.ico', '.jfif', '.heic', '.heif', '.exif'
    ],
    'Documents': [
        '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.epub',
        '.mobi', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.wps'
    ],
    'Data': [
        '.json', '.xml', '.sql', '.yaml', '.ini',
        '.log', '.db', '.mdb', '.accdb', '.sav', '.dat'
    ],
    'Scripts': [
        '.py', '.js', '.java', '.c', '.cpp', '.c#', '.asm', '.sh',
        '.bat', '.pl', '.rb', '.php', '.swift', '.go', '.r', '.lua',
        '.scala', '.html', '.css'
    ],
    'Executables': [
        '.exe', '.msi', '.app', '.deb', '.rpm', '.apk', '.bin',
        '.jar', '.cmd', '.wsf', '.vbs'
    ],
    'Music': [
        '.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a',
        '.opus', '.aiff', '.cda'
    ],
    'Videos': [
        '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm',
        '.mpeg', '.mpg', '.3gp', '.qt', '.ts', '.m4v', '.vob'
    ],
    'Compressed': [
        '.zip', '.rar', '.tar', '.gz', '.bz2', '.7z', '.xz',
        '.iso', '.cab', '.dmg'
    ],
    'Fonts': [
        '.ttf', '.otf', '.woff', '.woff2', '.fnt', '.pfb', '.pfm'
    ],
    'Backup': [
        '.bak', '.old', '.backup', '.tmp', '.swp', '.part', '.dmp'
    ],
    'Presentations': [
        '.ppt', '.pptx', '.key', '.odp', '.sxi'
    ],
    'Spreadsheets': [
        '.xls', '.xlsx', '.ods', '.csv', '.tsv', '.dif', '.slk'
    ],
    'Web Files': [
        '.html', '.htm', '.css', '.js', '.xml', '.json',
        '.csv', '.svg', '.php'
    ],
    'Other': []  # Category for unclassified files
}

def create_folders(base_dir):
    """Create necessary folders based on the defined categories."""
    for folder in extensions.keys():
        folder_path = os.path.join(base_dir, folder)
        # Check if the folder already exists; if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(base_dir):
    """Move files to their corresponding folders based on their extensions."""
    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, ext = os.path.splitext(file)
            moved = False
            # Check each category to find the correct destination
            for folder, file_extensions in extensions.items():
                if ext.lower() in file_extensions:
                    # Move the file to the corresponding folder
                    destination_path = os.path.join(base_dir, folder, file)
                    os.rename(file_path, destination_path)
                    moved = True
                    break
            # If no matching category was found, move to 'Other'
            if not moved:
                destination_path = os.path.join(base_dir, 'Other', file)
                os.rename(file_path, destination_path)

def organize_files(directory):
    """Organize the files in the specified directory."""
    create_folders(directory)  # Create necessary folders
    move_files(directory)       # Move files to the corresponding folders

def get_directory():
    """Prompt the user to select a directory to organize."""
    while True:
        print("Which directory do you want to organize?")
        print("1. The current directory")
        print("2. One directory back")
        print("3. One directory forward (create if not exists)")
        print("4. Specify a directory")
        option = input("Select an option (1-4): ")

        # Handle user input based on selected option
        if option == '1':
            return os.getcwd()  # Return the current directory
        elif option == '2':
            return os.path.dirname(os.getcwd())  # Return one directory back
        elif option == '3':
            new_directory = input("Enter the name of the new directory: ")
            directory = os.path.join(os.getcwd(), new_directory)
            # Create the new directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
            return directory
        elif option == '4':
            directory = input("Enter the path of the directory you want to organize: ")
            # Check if the specified directory exists
            if os.path.isdir(directory):
                return directory
            else:
                print("The directory does not exist. Please try again.")
        else:
            print("Invalid option. Please select between 1 and 4.")

def main():
    """Main function to organize files in the specified directory."""
    directory = get_directory()  # Get the directory from the user
    organize_files(directory)     # Organize files in that directory
    print(f"Files organized in the directory: {directory}")

if __name__ == "__main__":
    main()  # Execute the main function
