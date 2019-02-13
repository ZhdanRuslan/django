import lxml.html

from .models import Vacancy


def parse_vacancy(html_data):
    html_data = lxml.html.fromstring(html_data)
    title = html_data.find_class('f-visited-enable ga_listing')
    company = html_data.find_class('f-text-dark-bluegray f-visited-enable')
    preview = html_data.find_class('f-vacancylist-shortdescr')
    if title:
        for title, company, preview in zip(title, company, preview):
            title = title.get('title')
            company = company.get('title')
            preview = preview.text_content()

            Vacancy.objects.create(company=company, position=title, title=preview)

