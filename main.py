from flask import Flask, url_for, render_template
from facts import facts
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

text = """Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!""".split('\n')


@app.route('/')
def main_page():
    return render_template('base.html', title="Миссия Колонизация Марса")


@app.route('/index')
def index():
    return render_template('base.html',
                           title="И на Марсе будут яблони цвести!",
                           content="И на Марсе будут яблони цвести!")


@app.route('/index/<title>')
def index_with_title(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    a = [str(i) for i in text]
    return render_template('base.html',
                           title="Рекламная кампания",
                           content='</br>'.join(a))


@app.route('/image_mars')
def image_mars():
    content = f'''
           <h1>Жди нас, Марс!</h1>
           <img src="{url_for('static', filename='img/MARS.png')}"
           alt="здесь должна была быть картинка, но не нашлась"
           style="max-width: 100%; height: auto;">
           <h5>Вот она какая, красная планета.</h5>'''
    return render_template('base.html',
                           title="Жди нас, Марс!",
                           content=content)


@app.route('/choice/<choicePlanet>')
def choice(choicePlanet):
    choicePlanet = choicePlanet.lower()
    if choicePlanet in facts:
        content = f'''
        <h1>Мое предложение: {choicePlanet.capitalize()}</h1>
        <div class="alert alert-light" role="alert">
            {facts[choicePlanet][0]}
        </div>
        <div class="alert alert-primary" role="alert">
            {facts[choicePlanet][1]}
        </div>
        <div class="alert alert-warning" role="alert">
            {facts[choicePlanet][2]}
        </div>
        <div class="alert alert-dark" role="alert">
            {facts[choicePlanet][3]}
        </div>
        <div class="alert alert-danger" role="alert">
            {facts[choicePlanet][4]}
        </div>
        '''
        return render_template('base.html',
                               title=f"Мое предложение: {choicePlanet.capitalize()}",
                               content=content)
    else:
        content = "<h1>КРИТИЧЕСКАЯ ОШИБКА!!!!!!!!!!!</h1>"
        return render_template('base.html',
                               title="Ошибка",
                               content=content)


@app.route('/promotion_image')
def promotion_image():
    content = f'''
           <h1>Жди нас, Марс!</h1>
           <img src="{url_for('static', filename='img/MARS.png')}"
           alt="здесь должна была быть картинка, но не нашлась"
           style="max-width: 100%; height: auto;">
           <div class="alert alert-success" role="alert">
               Человечество вырастает из детства.
           </div>
           <div class="alert alert-primary" role="alert">
               Человечеству мала одна планета.
           </div>
           <div class="alert alert-warning" role="alert">
               Мы сделаем обитаемыми безжизненные пока планеты.
           </div>
           <div class="alert alert-dark" role="alert">
               И начнем с Марса!
           </div>
           <div class="alert alert-danger" role="alert">
               Присоединяйся!
           </div>
        '''
    return render_template('base.html',
                           title="Промо-изображение",
                           content=content)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    content = f'''
        <h1>Результаты отбора</h1>
        <h2>Претендент на участие в миссии {nickname}</h2>
        <div class="alert alert-success" role="alert">
            Поздравляем! Ваш рейтинг после {level} отбора
        </div>
        <div class="alert alert-info" role="alert">
            Составляет {rating}!
        </div>
        <div class="alert alert-warning" role="alert">
            Желаем удачи!
        </div>
    '''
    return render_template('base.html',
                           title="Результаты отбора",
                           content=content)


@app.route('/training/<string:prof>')
def training(prof):
    return render_template('training.html',
                           title="Тренировка",
                           prof=prof.capitalize())


@app.route('/list_prof/<string:marker>')
def list_prof(marker):
    professions = ["Инженер-исследователь",
                   "Инженер-строитель",
                   "Пилот",
                   "Метеоролог",
                   "Инженер по жизнеобеспечению",
                   "Инженер по радиационной защите",
                   "Врач",
                   "Экзобиолог"]
    return render_template('marker.html',
                           title="Список профессий",
                           prof=professions,
                           marker=marker)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    data = {
        'title': 'Анкета',
        'surname': 'Альберт',
        'name': 'Энштейн',
        'education': 'высшее',
        'profession': 'физик',
        'sex': 'male',
        'motivation': 'Это моя мечта!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
