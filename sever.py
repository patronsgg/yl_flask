from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    return render_template('index.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')