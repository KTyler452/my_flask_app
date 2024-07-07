# Title: web_app.py
# Abstract: Creates a app that displays information.
# Author: Tyler Pesl
# Date: 7/5/2024
# Class: CST205
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<html><body>
                <p>Shane S. : AFK</p>
                <p>Carson M. : lol</p>
                <p>Rene R. : brb</p>
                </body></html>'''

@app.route('/Tyler')
def show_template():
    return render_template('template.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap_template.html')

if __name__ == '__main__':
    app.run(debug=True)