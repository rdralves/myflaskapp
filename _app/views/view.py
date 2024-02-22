from flask import render_template, request, redirect, url_for
from _app import app
from _app.controllers import *
@app.route('/')
def index():
    return render_template('index.html')
