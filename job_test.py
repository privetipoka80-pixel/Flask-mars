from requests import get
from pprint import pprint

pprint(get('http://localhost:8080/api/jobs').json())
print('\n++++++++++++++++++++++++++++++++\n')

pprint(get('http://localhost:8080/api/jobs/1').json())
print('\n++++++++++++++++++++++++++++++++\n')

pprint(get('http://localhost:8080/api/jobs/999').json())
# новости с id = 999 нет в базе
print('\n++++++++++++++++++++++++++++++++\n')

pprint(get('http://localhost:8080/api/jobs/q').json())
