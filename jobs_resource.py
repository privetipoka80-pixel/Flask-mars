from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.jobs import Job
from data.reqparse_jobs import parser


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(jobs_id)
    if not jobs:
        abort(404, message=f"Jobs {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.get(Job, jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.get(Job, jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        jobs = db_sess.get(Job, jobs_id)
        jobs.team_leader = args['team_leader']
        jobs.job = args['job']
        jobs.work_size = args['work_size']
        jobs.collaborators = args['collaborators']
        jobs.is_finished = args['is_finished']
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Job).all()
        return jsonify({'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Job(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished'],
        )
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})