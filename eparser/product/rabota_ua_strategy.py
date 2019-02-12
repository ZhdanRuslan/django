import lxml.html

from eparser.product.base_strategy import Strategy
from eparser.product.module_settings import CITY
from eparser.product.models import Vacancy


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
            for title, company, preview in zip(title, company, preview):
                title = title.get('title')
                company = company.get('title')
                short_descr = preview.text_content()
                print('Vacancy: {}, Company: {}, {}'.format(title, company, CITY))
                print(short_descr.text_content())
                v = Vacancy.create(title, company, short_descr)