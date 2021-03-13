from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('index.html', list=list, list_prof=['Инженер-исследователь', 'Пилот', 'Строитель',
                                                               'Экзобиолог', 'Врач', 'Инженер по терраформированию',
                                                               'Климатолог', 'Специалист по радиационной защите',
                                                               'Астрогеолог', 'Гляциолог', 'Инженер жизнеобеспечения',
                                                               'Метеоролог', 'Оператор марсохода', 'Киберинженер',
                                                               'Штурман', 'Пилот дронов'])


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')