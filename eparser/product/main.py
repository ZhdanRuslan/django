import asyncio

from eparser.product.parser_rabota_ua import parse_urls, deep_parse
from eparser.product.parsers_settings import REQUEST_URL
from eparser.product.tools import async_request


def start_app():
    # loop = asyncio.get_event_loop()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    list_urls = []
    [list_urls.append(REQUEST_URL + str(i)) for i in range(1, 30)]
    result = loop.run_until_complete(async_request(list_urls))
    url_of_vac = parse_urls(result)
    result_full_vac_html = loop.run_until_complete(async_request(url_of_vac))
    loop.close()
    deep_parse(result_full_vac_html)


if __name__ == "__main__":
    start_app()
