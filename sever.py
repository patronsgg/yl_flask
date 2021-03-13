from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class AccessForm(FlaskForm):
    id_astronaut = StringField('ID астронавта', validators=[DataRequired(message='Необходимо выбрать значение')])
    password_astronaut = PasswordField('Пароль', validators=[DataRequired(message='Необходимо выбрать значение')])
    id_captain = StringField('ID капитана', validators=[DataRequired(message='Необходимо выбрать значение')])
    password_captain = PasswordField('Пароль', validators=[DataRequired(message='Необходимо выбрать значение')])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AccessForm()
    if form.validate_on_submit():
        return "Доступ разрешен"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')