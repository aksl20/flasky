from flask import render_template, flash, redirect, url_for
from app import app
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
  user = {'username' : 'Miguel'}
  posts = [
    {
      'author': {'username':'John'},
      'body': 'Beautiful day in Portland!'
    },
    {
      'author': {'username': 'Susan'},
      'body': 'The Avengers movie was so cool!'
    } 

  ]
  return render_template('index.html', title='Home', user=user, posts=posts) 

