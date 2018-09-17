from flask import Flask, render_template, redirect, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def index():
    if 'counter' in session:
        print(session)
        session['counter'] = session.get('counter') + 1
        print(session['counter'])
    else:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])


@app.route('/addTwo')
def addTwo():
    if 'counter' in session:
        print(session)
        session['counter'] = session.get('counter') + 1
        print(session['counter'])
    else:
        session['counter'] = 1
    return redirect('/')


@app.route('/beGone')
def beGone():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
