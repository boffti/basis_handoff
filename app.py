from flask import Flask, render_template, request, redirect, url_for, session
from database import db_session
from models import Handoff
import utils
import json
import logging
import os

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['ENV'] = 'development'


logging.basicConfig(filename="kutty.log",
                    format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@app.route('/')
def home():
      if not session.get('logged_in'):
            return render_template('login.html')
      else:
            return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_handler():
      error = None
      if request.method == 'POST':
            if request.form['fUser'] != 'admin' or request.form['fPassword'] != 'admin':
                  error = 'Invalid Credentials. Please try again.'
            else:
                  session['logged_in'] = True
                  return redirect(url_for('home'))
      return render_template('login.html', error=error)


@app.route('/add_priority_task')
def addPriorityTask():
    return render_template('expression')




@app.route("/logout")
def logout():
      session['logged_in'] = False
      return home()


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5050, debug=True)
