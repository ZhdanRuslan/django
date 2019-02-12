import lxml.html

SPECIALIZATION = '/python'
CITY = 'KIEV'
CITY_DICT = {
    'KIEV': '/киев',
}
BASE_URL = 'https://rabota.ua/zapros/'
REQUEST_URL = BASE_URL + SPECIALIZATION + CITY_DICT.get(CITY)


async def parse_vacancy(html):
    html = lxml.html.fromstring(html)
    title = html.find_class('f-visited-enable ga_listing')
    company = html.find_class('f-text-dark-bluegray f-visited-enable')

    if title:
        for vacancy, company in zip(title, company):
            print('Vacancy: {}, Company: {}, {}'.format(vacancy.get('title'), company.get('title'),
                                                        CITY))