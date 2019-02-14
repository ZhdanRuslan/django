import lxml.html
from .parsers_settings import CITY
from .tools import async_request

from .models import Vacancy

URL_RABOTA_UA = 'https://rabota.ua/'
vacancy_urls = []


#
# def parse_vacancy(html_data):
#     html_data = lxml.html.fromstring(html_data)
#     title = html_data.find_class('f-visited-enable ga_listing')
#     company = html_data.find_class('f-text-dark-bluegray f-visited-enable')
#     preview = html_data.find_class('f-vacancylist-shortdescr')
#     href = html_data.find_class('f-visited-enable ga_listing')
#     if title:
#         for title, company, preview, href in zip(title, company, preview, href):
#             title = title.get('title')
#             company = company.get('title')
#             preview = preview.text_content()
#             href = href.get(URL_RABOTA_UA + 'href')
#             print(href)
#             Vacancy.objects.create(company=company, position=title, title=preview)


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

    for position, company, description in zip(positions, companies, descriptions):
        position = position.text_content()
        company = company.text_content()
        description = description.text_content()[41:]

        Vacancy.objects.create(position=position, company=company, description=description, city=CITY)

