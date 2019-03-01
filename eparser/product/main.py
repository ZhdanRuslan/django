import aiohttp

from .parser_rabota_ua import parse_urls, deep_parse
from .tools import fetch_all


async def start_app(url):
    async with aiohttp.ClientSession() as session:
        list_urls = [url]
        [list_urls.append(url + '/pg' + str(i)) for i in range(2, 30)]
        result = await fetch_all(session, list_urls)
        url_of_vac = parse_urls(result)
        result_full_vac_html = await fetch_all(session, url_of_vac)
        deep_parse(result_full_vac_html)

