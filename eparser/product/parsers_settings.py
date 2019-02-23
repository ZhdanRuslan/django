SPECIALIZATION = '/python'
CITY = 'KIEV'
CITY_DICT = {
    'KIEV': '/киев',
    'KHARKOV': '/харьков',
    'ALL': '/украина',
}
BASE_URL = 'https://rabota.ua/zapros/'
REQUEST_URL = BASE_URL + SPECIALIZATION + CITY_DICT.get('ALL') + '/pg'