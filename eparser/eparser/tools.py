import aiohttp
import asyncio
import lxml.html


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2')
        html = lxml.html.fromstring(html)
        root = html.find_class('f-visited-enable ga_listing')

        if root:
            for vacancy in root:
                title = vacancy.text_content()
                title = title.strip()
                print(title)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
