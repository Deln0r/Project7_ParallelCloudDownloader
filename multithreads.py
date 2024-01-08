from queue import Queue
from threading import Thread
import time

from getfilelistpy import getfilelist
import gdown
THREAD_POOL_SIZE = 5

#update the resource object as per your API key and the gdriver folder id
resource = {
    "api_key": "##################",
    "id": "###################",
    "fields": "files(name,id,webContentLink)",
}

class DownlaodWorker(Thread):

    def __init__(self, name, queue):
        Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            # Get the file id and name from the queue
            item1 = self.queue.get()
            try:
                gdown.download( item1['webContentLink'],
                                './files/{}'.format(item1['name']),
                                quiet=False)
            finally:
                self.queue.task_done()

