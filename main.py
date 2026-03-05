from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main_page():
    return render_template('base.html')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    return render_template('training.html', prof=prof.capitalize())


@app.route('/list_prof/<string:marker>')
def list_prof(marker):
    professions = ["Инженер-исследователь",
                   "Инженер-строитель",
                   "Пилот", "Метеоролог",
                   "Инженер по жизнеобеспечению",
                   "Инженер по радиационной защите",
                   "Врач", "Экзобиолог"]
    return render_template('marker.html', prof=professions, marker=marker)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
