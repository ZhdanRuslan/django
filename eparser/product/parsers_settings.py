SPECIALIZATION = 'All'
SPECIALIZATION_DICT = {
    'All': 'developer',
    'Java': 'java',
    'Python': 'python',
    'JavaScript': 'javascript',
    'PHP': 'php',

}
CITY = 'KIEV'
CITY_DICT = {
    'Kiev': '/киев',
    'Kharkov': '/харьков',
    'All': '/украина',
}
BASE_URL = 'https://rabota.ua/zapros/'
REQUEST_URL = BASE_URL + SPECIALIZATION_DICT.get('All') + CITY_DICT.get('All') + '/pg'
