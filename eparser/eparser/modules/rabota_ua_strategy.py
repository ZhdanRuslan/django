import lxml.html

from eparser.eparser.modules.base_strategy import Strategy
from eparser.eparser.modules.module_settings import CITY


class ParseRabotaUa(Strategy):
    """
    Concrete strategy for parse rabota.ua
    """

    def parse_vacancy(self, html_data):
        html_data = lxml.html.fromstring(html_data)
        title = html_data.find_class('f-visited-enable ga_listing')
        company = html_data.find_class('f-text-dark-bluegray f-visited-enable')

        if title:
            for vacancy, company in zip(title, company):
                print('Vacancy: {}, Company: {}, {}'.format(vacancy.get('title'), company.get('title'),
                                                            CITY))