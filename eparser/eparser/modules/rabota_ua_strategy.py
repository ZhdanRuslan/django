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
        preview = html_data.find_class('f-vacancylist-shortdescr')

        if title:
            for vacancy, company, short_descr in zip(title, company, preview):
                print('Vacancy: {}, Company: {}, {}'.format(vacancy.get('title'), company.get('title'),
                                                            CITY))
                print(short_descr.text_content())