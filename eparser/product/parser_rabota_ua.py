import logging

import lxml.html
from .parsers_settings import CITY

from .models import Vacancy

URL_RABOTA_UA = 'https://rabota.ua/'
vacancy_urls = []


def parse_urls(html_data):
    html_data = lxml.html.fromstring(html_data)
    hrefs = html_data.find_class('f-visited-enable ga_listing')
    if hrefs:
        for href in hrefs:
            vacancy_urls.append(URL_RABOTA_UA + href.get('href'))

    return vacancy_urls


def deep_parse(html_data):
    html_data = lxml.html.fromstring(html_data)
    positions = html_data.find_class('f-vacname-holder')
    companies = html_data.find_class('fd-soldier')
    descriptions = html_data.find_class('f-vacancy-description')
    # vac_from_db = set(Vacancy.objects.all())
    for position, company, description in zip(positions, companies, descriptions):
        position = position.text_content()
        company = company.text_content()
        description = description.text_content()[41:]
        if Vacancy.objects.filter(position=position, company=company, description=description, city=CITY):
            continue
        else:
            Vacancy.objects.create(position=position, company=company, description=description, city=CITY)
    logging.debug('Parsed {} vacancies from {}'.format(len(positions), URL_RABOTA_UA))
