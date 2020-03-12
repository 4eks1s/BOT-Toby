import os
import git

from threading import Thread
from time import sleep

os.environ["BOT_UPGRADE"] = "no"

def threaded_function():
    while(True):
        if os.getenv("BOT_UPGRADE") == "yes":
            repo = git.Repo(os.getcwd())
            o = repo.remotes.origin
            o.pull()
        sleep(1)

def start():
    exec(open('bot.py').read())
    start()

thread = Thread(target = threaded_function)
thread.start()

start()

