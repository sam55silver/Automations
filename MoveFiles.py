# By Sam Silver
# March 3rd 2021

import os


def check_config():
    # Opens config to get folder to track
    if os.path.exists("moveFilesConfig.txt"):
        file = open("moveFilesConfig.txt", "r")
        folder_to_track = file.read()
        file.close()
    else:  # If file does not exist then make one!
        print("No config file found...")
        folder_to_track = input(
            "What path would you like me to track from here on out: ")

        while not(os.path.exists(folder_to_track)):  # Make sure the entered dir exists
            folder_to_track = input(
                "That path does not exist... please re-enter:")

        print("Creating config...\n")

        file = open("moveFilesConfig.txt", "w")
        file.write(folder_to_track)
        file.close
    return folder_to_track


def sort_files(folder_to_track):
    # Loop through array of directory and sort each file
    filesMoved = 0
    for file in os.listdir(folder_to_track):
        if file in folder_names:  # Check if its looking at one of the folders we have created above
            continue
        destination = check_file_copies(check_file_extension(file), file)
        print(f"Moving {file} to {destination} \n")
        os.rename(folder_to_track + "/" + file, destination)
        filesMoved += 1
    print(f"Moved {str(filesMoved)} files\nSo long!")


def check_file_extension(filename):
    # Look at the extension the file has and assign appropriate destination
    if filename.lower().endswith('.mp3'):  # Music
        return folder_to_track + "/" + folder_names[6]

    elif filename.lower().endswith(('.xlsx', '.csv')):  # Spread Sheets
        return folder_to_track + "/" + folder_names[5]

    elif filename.lower().endswith(('.mov', '.avi', '.mp4')):  # Videos
        return folder_to_track + "/" + folder_names[4]

    elif filename.lower().endswith(('.pptx', '.ppt')):  # Power points
        return folder_to_track + "/" + folder_names[3]

    elif filename.lower().endswith(('.txt', '.pdf', '.docx')):  # Documents
        return folder_to_track + "/" + folder_names[2]

    elif filename.lower().endswith(('.jpg', '.png', '.heic', '.jpeg')):  # Images
        return folder_to_track + "/" + folder_names[1]

    else:  # Other
        return folder_to_track + "/" + folder_names[0]


def check_file_copies(destination, filename):
    # Loop through destination to see if there are any copies
    index = 0
    while os.path.exists(destination + "/" + filename):
        filename, extension = os.path.splitext(filename)
        if index == 0:
            filename = filename + "(0)" + extension
        else:
            filename = filename.replace(filename[-2], str(index)) + extension
        index += 1
    return destination + "/" + filename


# Check/Check config to retrive trackable path
folder_to_track = check_config()

# Destination folders
folder_names = ['other', 'images', 'documents',
                'powerpoints', 'videos', 'spreadsheets', 'audio']
# Create destinations if they do not exist
for names in folder_names:
    path = folder_to_track + '/' + names
    if not(os.path.exists(path)):
        print(f"{path} does not exist... creating it.")
        os.mkdir(path)

# Sort files in trackable path into individual files
sort_files(folder_to_track)
