import asyncio

from eparser.product.parsers.parser_rabota_ua import parse_vacancy
from eparser.product.parsers.parsers_settings import REQUEST_URL
from eparser.product.tools import async_request


def start_app():
    loop = asyncio.get_event_loop()
    list_urls = []
    [list_urls.append(REQUEST_URL + str(i)) for i in range(1, 30)]
    result = loop.run_until_complete(async_request(list_urls))
    parse_vacancy(result)


if __name__ == "__main__":
    start_app()
