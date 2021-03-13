from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def distribution(sex, age):
    return render_template('index.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')