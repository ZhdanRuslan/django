import asyncio

from .parser_rabota_ua import parse_urls, deep_parse
from .parsers_settings import REQUEST_URL
from .tools import async_request


def start_app(url=None):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print(f'main: {url}')
    list_urls = []
    if url is None:
        url = REQUEST_URL
    list_urls.append(url)
    [list_urls.append(url + str(i)) for i in range(2, 30)]

    for i in list_urls:
        print(i)
    result = loop.run_until_complete(async_request(list_urls))
    url_of_vac = parse_urls(result)

    result_full_vac_html = loop.run_until_complete(async_request(url_of_vac))
    loop.close()
    deep_parse(result_full_vac_html)


if __name__ == "__main__":
    start_app()
