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