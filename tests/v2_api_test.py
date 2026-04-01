from requests import get, post, delete, put
from pprint import pprint

pprint(get('http://localhost:8080/api/v2/users').json())
print('------------------')
pprint(post('http://localhost:8080/api/v2/users',
            json={'surname': 'aaaaafff', 'name':'rrrrrrrrrrrfff', 'age': 99, 'position': 'ghjk', 'speciality': 'rytju', 'address': 'dfgh', 'email': 'eew11@.gmail.com', 'hashed_password': 23456789}).json())
print('------------------')
pprint(get('http://localhost:8080/api/v2/users/1').json())
print('------------------')
pprint(delete('http://localhost:8080/api/v2/users/1').json())