from flask import render_template, request, redirect, url_for
from _app import app
from _app.controllers.controller import get_all, add, delete, update


@app.route('/')
def index():
    return render_template('index.html', data=get_all())

@app.route('/add', methods=['POST'])
def add_item():
    add(request.form['name'])
    return redirect(url_for('index'))

@app.route('/delete/<item_id>')
def delete_item(item_id):
    delete(item_id)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_item():
    update(request.form['name'], request.form['id'])
    return redirect(url_for('index'))
