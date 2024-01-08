import time
from multiprocessing import Process, JoinableQueue
from getfilelistpy import getfilelist
import gdown

PROCESSES_POOL_SIZE = 5

#update the resource object as per your API key and the gdriver folder id
resource = {
    "api_key": "####################",
    "id": "####################",
    "fields": "files(name,id,webContentLink)",
}

def mydownloader( queue):
    while True:
        # Get the file id and name from the queue
        item1 =  queue.get()
        try:
            gdown.download(item1['webContentLink'],
                           './files/{}'.format(item1['name']),
                           quiet=False)
        finally:
            queue.task_done()


def get_files(resource):
    res = getfilelist.GetFileList(resource)
    files_list = res['fileList'][0]
    return files_list
