from flask import Flask, url_for, render_template, request
from facts import facts
from data import db_session
from data.users import User
from data.jobs import Jobs
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")
db_sess = db_session.create_session()
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
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {}
    for user in users:
        names[user.id] = f'{user.surname} {user.name}'
    return render_template('index.html', jobs=jobs, names=names)


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


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    param = {}
    param['gender'] = gender
    param['age'] = age
    return render_template('table.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form['id_astronaut'], '')
        print(request.form['password_astronaut'], '')
        print(request.form['id_captain'], '')
        print(request.form['password_captain'], '')

        return "Доступ разрешен"


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Пейзажи Марса</h1>
                        <div id="carouselExample" class="carousel slide">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="/static/images_for_carusel/landscape1.jpg" class="d-block w-100" alt="landscape1" style="width: 1000px; height: 680px;">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/images_for_carusel/landscape2.jpg" class="d-block w-100" alt="landscape2" style="width: 1000px; height: 680px;">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/images_for_carusel/landscape3.jpg" class="d-block w-100" alt="landscape3" style="width: 1000px; height: 680px;">
                            </div>
                          </div>
                          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Предыдущий</span>
                          </button>
                          <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Следующий</span>
                          </button>
                        </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
                      </body>
                    </html>"""


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        if not os.path.exists('static/uploads'):
            os.makedirs('static/uploads')
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Загрузка фотографии</h1>
                                <h2>Для участия в миссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <img src="/static/uploads/photo.jpg" style="max-width: 300px; height: auto;">
                                        </br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        f.save('static/uploads/photo.jpg')
        return "Форма отправлена"


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претедента на участие в миссии</h1>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Профессиональное</option>
                                            </select>
                                         </div>
                                         <div class="form-group">
                                            <label for="form-check">Какие у вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof1" value="инженер-исследователь">
                                              <label class="form-check-label" for="prof1">инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof2" value="пилот">
                                              <label class="form-check-label" for="prof2">пилот</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof3" value="строитель">
                                              <label class="form-check-label" for="prof3">строитель</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof4" value="экзобиолог">
                                              <label class="form-check-label" for="prof4">экзобиолог</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof5" value="врач">
                                              <label class="form-check-label" for="prof5">врач</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof6" value="инженер по терраформированию">
                                              <label class="form-check-label" for="prof6">инженер по терраформированию</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof7" value="климатолог">
                                              <label class="form-check-label" for="prof7">климатолог</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof8" value="специалист по радиационной защите">
                                              <label class="form-check-label" for="prof8">специалист по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof9" value="астрогеолог">
                                              <label class="form-check-label" for="prof9">астрогеолог</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof10" value="гляциолог">
                                              <label class="form-check-label" for="prof10">гляциолог</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="sex_male" value="male" checked>
                                              <label class="form-check-label" for="sex_male">Мужской</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="sex_female" value="female">
                                              <label class="form-check-label" for="sex_female">Женский</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>

                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'], '')
        print(request.form['name'], '')
        print(request.form['email'], '')
        print(request.form['class'], '')
        print(', '.join(request.form.getlist('profession')))
        print(request.form['sex'], '')
        print(request.form['about'], '')
        f = request.files['file']
        print(f.read())
        print(request.form['accept'], '')

        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
