from flask import Flask, redirect, render_template, request, url_for
# from flask_login import UserMixin
# from flask_smysqldb import MySQL
# from flask_wtf import FlaskForm
# from wtforms import PasswordField, StringField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(_name_)
# cursor=connection.cursor()

# mysql= MySQL(app)

# app.config['MYSQL_USER']=' sql12659183'
# app.config['MYSQL_PASSWORD']='m2yzIXuIFA'
# app.config['MYSQL_HOST']='sql12.freemysqlhosting.net'
# app.config['MYSQL_DB']=' sql12659183'
# app.config['MYSQL_CURSORCLASS']='DictCursor'


# # self.init_app(app)

# class User(db.Model,UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     username= db.Column(db.String(20),nullable=false, unique=True)
#     password= db.Column(db.String(80),nullable=false)

# class signupForm(FlaskForm):
#     username= StringField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={"placeholder":"username"})
#     password= PasswordField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={"placeholder":"username"})
# submit=SubmitField("Reister")

# def validate_username(self,username):
#     existing_user_username = User.query.filter_by(username=username.data).first()
#     if existing_user_username:
#         raise ValidationError("The username already exist. Please choose differnt one.")

# class loginForm(FlaskForm):
#     username= StringField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={"placeholder":"username"})
#     password= PasswordField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={"placeholder":"username"})
# submit=SubmitField("Login")

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login')
def login():
    # cur= mysql.connection.cursor()
    # cur.execute('''CREATE TABLE log(username VARCHAR(15) password VARCHAR(15))''')
    # return 'Done!'
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
    
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/review/')
def review():
    return render_template('review.html')

@app.route('/about1/')
def about1():
    return render_template('about1.html')

@app.route('/books/')
def books():
    return render_template('books.html')

if _name_ =='_main_':
    app.run(debug=True)