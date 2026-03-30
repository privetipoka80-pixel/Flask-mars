from requests import get
from pprint import pprint

pprint(get('http://localhost:8080/api/v2/users/1').json())
print('\n++++++++++++++++++++++++++++++++\n')

