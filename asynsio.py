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
async def mydownloader(name, queue):
    while True:
        # Get the file id and name from the queue
        item = await queue.get()
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                async with session.get(item['webContentLink']) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open('./files/{}'.format(
                            item['name']), mode='wb')
                        await f.write(await resp.read())
                        await f.close()
        finally:
            print(f"{name}: Download completed for ",item['name'])
            queue.task_done()

def get_files(resource):
    res = getfilelist.GetFileList(resource)
    files_list = res['fileList'][0]
    return files_list
