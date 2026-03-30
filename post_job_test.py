from requests import post

print(post('http://localhost:8080/api/jobs', json={}).json())

print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1}).json())

print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1, 'collaborators': '1, 2', 'job': 'wasd', 'work_size': 1234, 'is_finished': False}).json())