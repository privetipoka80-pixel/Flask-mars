from data.users import User
from data import db_session
from data.jobs import Jobs

data = [{'team_leader': 1,
         'job': 'deployment of residential modules 1 and 2',
         'work_size': 15,
         'collaborators': '1, 3',
         'is_finished': False, },
        {'team_leader': 4,
         'job': 'deployment of residential modules 1 and 2',
         'work_size': 17,
         'collaborators': '5, 3',
         'is_finished': False, },
        {'team_leader': 2,
         'job': 'deployment of residential modules 1 and 2',
         'work_size': 20,
         'collaborators': '6, 3',
         'is_finished': True, },
        {'team_leader': 3,
         'job': 'deployment of residential modules 1 and 2',
         'work_size': 25,
         'collaborators': '7, 3',
         'is_finished': True, }]


def insert_jobs():
    for elem in data:
        job = Jobs()
        job.team_leader = elem['team_leader']
        job.job = elem['job']
        job.work_size = elem['work_size']
        job.collaborators = elem['collaborators']
        job.is_finished = elem['is_finished']
        db_sess = db_session.create_session()
        db_sess.add(job)
        db_sess.commit()


db_session.global_init("db/mars_explorer.db")
insert_jobs()
