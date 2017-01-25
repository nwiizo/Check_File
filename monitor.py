#!/usr/bin/python

import pyinotify,subprocess

# Directory to watch
# We'll use the shared volume with docker container
directory_to_watch = str(input("watch_dir:"))

def onChange(ev):
    # Print changed file on the screen
    # But could be your code to upload the file to VirusTotal
    # Or anything you want
    cmd = ['/bin/echo', 'File', ev.pathname, 'changed']
    subprocess.Popen(cmd).communicate()

wm = pyinotify.WatchManager()
wm.add_watch(directory_to_watch, pyinotify.IN_CLOSE_WRITE, onChange)
notifier = pyinotify.Notifier(wm)
notifier.loop()
