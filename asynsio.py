import asyncio
import time

import aiofiles, aiohttp
from getfilelistpy import getfilelist

TASK_POOL_SIZE = 10

#update the resource object as per your API key and the gdriver folder id
resource = {
    "api_key": "#######################",
    "id": "##################",
    "fields": "files(name,id,webContentLink)",
}
