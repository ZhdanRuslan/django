import aiohttp
import asyncio

from eparser.eparser.modules.rabota import parse_vacancy, REQUEST_URL


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def async_request(REQUEST_URL):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, REQUEST_URL)
        await parse_vacancy(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(async_request(REQUEST_URL))
