import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_modified(event):
    filename = event.src_path.replace(folder_to_track, "")
    destination = folder_documents + filename
    os.rename(event.src_path, destination)
    print(f"Moved {filename} to {destination}")


my_event_handler.on_modified = on_modified

folder_to_track = "D:\\Development\\Test\\myFolder"
folder_images = "D:\\Development\\Test\\images"
folder_documents = "D:\\Development\\Test\\documents"

go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, folder_to_track,
                     recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
