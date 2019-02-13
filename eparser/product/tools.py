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


