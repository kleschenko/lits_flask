from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(200), unique=True)
    name = db.Column(db.String(100))

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def pretty_print_user(self):
        return 'Username: %s, name: %s' % (self.username, self.name)

    def upper_name(self):
        return self.name.upper()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey(User.id))
