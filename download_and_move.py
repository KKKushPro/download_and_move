import time
import shutil
import os

from watchdog.observers import Observer
from watchdog.events import FilesSystemEventHandler
fromdir = "C:/Users/kush2/Downloads"

class FileMovementHandler (FilesSystemEventHandler):
    def on_created(self, event):
        print(event)

    
eventHandler = FileMovementHandler()
observer = Observer()
observer.schedule(eventHandler, fromdir, recurrsive=True)
observer.start()

while True:
    time.sleep(2)
    print("running")
