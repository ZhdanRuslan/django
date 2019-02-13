import lxml.html

from eparser.product.base_strategy import Strategy
from eparser.product.tools import Vacancy


class ParseRabotaUa(Strategy):
    """
    Concrete strategy for parse rabota.ua
    """

    def parse_vacancy(self, html_data):
        html_data = lxml.html.fromstring(html_data)
        title = html_data.find_class('f-visited-enable ga_listing')
        company = html_data.find_class('f-text-dark-bluegray f-visited-enable')
        preview = html_data.find_class('f-vacancylist-shortdescr')
        result_list = list()
        if title:
            for title, company, preview in zip(title, company, preview):
                title = title.get('title')
                company = company.get('title')
                preview = preview.text_content()

                vac = Vacancy(title, company, preview)
                print(vac)

                result_list.append(vac)

        return result_list
