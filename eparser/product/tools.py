import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()


async def async_request(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        return str(await asyncio.gather(*tasks))


class Vacancy():

    def __init__(self, company, position, short_descr):
        self.company = company
        self.position = position
        self.short_desct = short_descr

    def __str__(self):
        return '{} in {}'.format(self.company, self.position)

