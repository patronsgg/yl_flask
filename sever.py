from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    return render_template('index.html', persons=['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                                                  'Венката Капур', 'Тедди Сандерс', 'Шон Бин'])


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')