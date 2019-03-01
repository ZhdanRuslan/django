import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_all(session, urls):

    results = await asyncio.gather(*[asyncio.create_task(fetch(session, url))
                                     for url in urls])
    return str(results)
