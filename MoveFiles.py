import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# initialize event handler
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


# If Folder To Track is added to... do the following
def on_modified(event):
    # Obtain the filename of file being added
    filename = event.src_path.replace(folder_to_track, "")

    # Look at the extension the file has and assign appropriate destination
    if filename.lower().endswith('.txt'):
        destination = folder_documents + filename
    elif filename.lower().endswith('.jpg'):
        destination = folder_images + filename
    else:
        destination = folder_other + filename

    # Move to the destination
    os.rename(event.src_path, destination)
    print(f"Moved {filename} to {destination}")


# Add on_modified to the list of events to look out for
my_event_handler.on_modified = on_modified

# Folder destinations
folder_to_track = "D:\\Development\\Test\\myFolder"
folder_images = "D:\\Development\\Test\\images"
folder_documents = "D:\\Development\\Test\\documents"
folder_other = "D:\\Development\\Test\\other"

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
    print("So long!")
    my_observer.stop()
    my_observer.join()
