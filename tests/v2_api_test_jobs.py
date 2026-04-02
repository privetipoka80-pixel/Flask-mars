from requests import get, post, delete, put
from pprint import pprint

pprint(get('http://localhost:8080/api/v2/jobs/').json())
print('------------------')
print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 2,
                 'job': 'proger',
                 'collaborators': '1, 2',
                 'work_size': 22,
                 'is_finished': True}).json())
print('------------------')
pprint(get('http://localhost:8080/api/v2/jobs/1').json())
print('------------------')
pprint(delete('http://localhost:8080/api/v2/jobs/1').json())
