import logging

import lxml.html
from .parsers_settings import CITY
from .models import Vacancy

logging.basicConfig(level=logging.INFO)

URL_RABOTA_UA = 'https://rabota.ua/'


def parse_urls(html_data):
    vacancy_urls = []
    html_data = lxml.html.fromstring(html_data)
    hrefs = html_data.find_class('f-visited-enable ga_listing')
    if hrefs:
        for href in hrefs:
            vacancy_urls.append(URL_RABOTA_UA + href.get('href'))
    return vacancy_urls


def deep_parse(html_data_str):
    html_data = lxml.html.fromstring(html_data_str)
    positions = html_data.find_class('f-vacname-holder')
    companies = html_data.find_class('fd-soldier')
    descriptions = html_data.find_class('f-vacancy-description')
    for position, company, description in zip(positions, companies, descriptions):
        position = position.text_content()
        company = company.text_content()
        description = description.text_content()[41:]
        if Vacancy.objects.filter(position=position, company=company, description=description, city=CITY):
            continue
        else:
            Vacancy.objects.create(position=position, company=company, description=description, city=CITY)
    logging.info('Parsed {} vacancies from {}'.format(len(positions), URL_RABOTA_UA))
