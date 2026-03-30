import os

from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Job
from forms.login import LoginForm
from forms.user import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user
from data import db_session, jobs_api
from flask import make_response, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
answers = {
    'title': 'Анкета',
    'surname': 'Watny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': 'True'
}
db_session.global_init("db/mars.db")
db_sess = db_session.create_session()
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User,user_id)


@app.route('/')
@app.route('/index')
def index(**param):
    jobs = db_sess.query(Job).all()
    users = db_sess.query(User).all()
    names = {}
    for user in users:
        names[user.id] = f"{user.surname} {user.name}"
    print(names)
    return render_template('index.html', jobs=jobs, names=names, **param)











def main():
    db_session.global_init("db/mars.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()