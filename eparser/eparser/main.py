import asyncio

from eparser.eparser.modules.base_strategy import Context
from eparser.eparser.modules.module_settings import REQUEST_URL
from eparser.eparser.modules.rabota_ua_strategy import ParseRabotaUa
from eparser.eparser.tools import async_request


def main():
    loop = asyncio.get_event_loop()
    rabota_ua_strategy = ParseRabotaUa()
    context = Context(rabota_ua_strategy)
    l = []
    [l.append(REQUEST_URL + str(i)) for i in range(1, 10)]

    for i in l:
        result = loop.run_until_complete(async_request(i))
        context.parse_vacancy(result)


if __name__ == "__main__":
    main()
