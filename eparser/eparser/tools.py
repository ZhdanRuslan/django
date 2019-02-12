import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def async_request(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url=url)
        return html
