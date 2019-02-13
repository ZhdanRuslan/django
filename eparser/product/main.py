import asyncio

from .parser_rabota_ua import parse_vacancy
from .parsers_settings import REQUEST_URL
from .tools import async_request


def start_app():
    # loop = asyncio.get_event_loop()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    list_urls = []
    [list_urls.append(REQUEST_URL + str(i)) for i in range(1, 30)]
    result = loop.run_until_complete(async_request(list_urls))
    loop.close()
    parse_vacancy(result)


if __name__ == "__main__":
    start_app()
