import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# Retrive users destination for folders
folder_to_track = input("What path am I tracking today: ")
# Debug purposes... Not trying to enter every time
# Add a config file later
if folder_to_track == 'mac':
    folder_to_track = '/Users/sam/Down'
elif folder_to_track == 'win':
    folder_to_track = 'D:/Development/Test/myFolder'

# Destination folders
folder_names = ['other', 'images', 'documents']
# Create destinations if they do not exist
for names in folder_names:
    path = folder_to_track + '/' + names
    if not(os.path.exists(path)):
        print(f"{path} does not exist... creating it.")
        os.mkdir(path)
    else:
        print(f"{path} exists")  # DEBUG PURPOSE GET RID

# initialize event handler
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    # Obtain the filename of file being added
    filename = event.src_path.replace(folder_to_track, "")
    print(f"created an item {event.src_path}")
    path = event.src_path

    # Look at the extension the file has and assign appropriate destination
    if filename.lower().endswith('.txt'):
        destination = folder_to_track + "/" + folder_names[2]
    elif filename.lower().endswith('.jpg'):
        destination = folder_to_track + "/" + folder_names[1]
    else:
        destination = folder_to_track + "/" + folder_names[0]

    # Loop through destination to see if there are any copies
    index = 0
    while os.path.exists(destination + filename):
        filename, extension = os.path.splitext(filename)
        if index == 0:
            filename = filename + "(0)" + extension
        else:
            filename = filename.replace(filename[-2], str(index)) + extension
        index += 1

    try:
        os.rename(path, destination + filename)
    except FileNotFoundError:  # If we are faced with no file make sure it does not crash file
        print("You are probs copying and pasting... do not do that")

    # Move to the destination
    print(f"Moved {filename} to {destination}\n")


# Look out for when a file is created in a folder, if so do function on_created
my_event_handler.on_created = on_created

# Setup observer with the event handler and folder to watch
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, folder_to_track,
                     recursive=go_recursively)

# Start up observer
my_observer.start()
print(f"I have got my eyes on {folder_to_track}...\n")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:  # Stop program with keyboard interruption
    print("\nSo long!")
    my_observer.stop()
    my_observer.join()
