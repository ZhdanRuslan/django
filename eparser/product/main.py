import asyncio

from base_strategy import Context
from module_settings import REQUEST_URL
from rabota_ua_strategy import ParseRabotaUa
from tools import async_request


def main():
    loop = asyncio.get_event_loop()
    rabota_ua_strategy = ParseRabotaUa()
    context = Context(rabota_ua_strategy)
    list_urls = []
    [list_urls.append(REQUEST_URL + str(i)) for i in range(1, 30)]

    # print(list_urls)
    result = loop.run_until_complete(async_request(list_urls))
    context.parse_vacancy(result)


if __name__ == "__main__":
    main()
