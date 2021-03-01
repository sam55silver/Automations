from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            # Insert file into images folder
            if filename.lower().endswith('.jpg'):
                new_destination = folder_images + "/" + filename
                os.rename(src, new_destination)
            # Insert File into document folder
            elif filename.lower().endswith('.pdf'):
                new_destination = folder_documents + "/" + filename
                os.rename(src, new_destination)


folder_to_track = "/Users/sam/Desktop/myFolder"
folder_images = "/Users/sam/Desktop/images"
folder_documents = "/Users/sam/Desktop/documents"
folder_destination = "/Users/sam/Desktop/newFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
