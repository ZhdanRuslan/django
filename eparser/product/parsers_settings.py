SPECIALIZATION = '/java'
CITY = 'KIEV'
CITY_DICT = {
    'KIEV': '/киев',
    'KHARKOV': '/харьков',
}
BASE_URL = 'https://rabota.ua/zapros/'
REQUEST_URL = BASE_URL + SPECIALIZATION + CITY_DICT.get(CITY) + '/pg'