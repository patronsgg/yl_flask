from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer/')
@app.route('/auto_answer/')
def answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = ('Фамилия:', 'Watny')
    param['name'] = ('Имя:', 'Mark')
    param['education'] = ('Образование:', 'выше среднего')
    param['profession'] = ('Профессия:', 'штурман марсохода')
    param['sex'] = ('Пол:', 'male')
    param['motivation'] = ('Мотивация:', 'Всегда мечтал застрять на Марсе!')
    param['ready'] = ('Готовы остаться на Марсе?', 'True')
    return render_template('auto_answer.html', param=param)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')