import flask

from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask('flask_app')
app.config.from_object('config')
db = SQLAlchemy(app)

db.create_all()


admin_user = {
    'username': 'admin',
    'password': 'admin'
}


@app.route('/')
def main():
    title = 'my title'
    user = {'nickname': 'Some name'}
    return flask.render_template(
        'index.html',
        title=title,
        user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Username:', form.data['username'])
        print('Password:', form.data['password'])
        if (form.data['username'] == admin_user['username']
                and form.data['password'] == admin_user['password']):
            return flask.redirect('/')
        else:
            flask.flash('Wrong username!')
    return flask.render_template('login.html', form=form)


import models

if __name__ == '__main__':
    app.run(debug=True)
