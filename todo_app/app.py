from turtle import title
from flask import Flask
from flask import render_template, request, redirect

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items = items)

@app.route('/add', methods=['POST'])
def add():
    title = request.form["todo"]
    todo = add_item(title)
    return redirect('/')
    
 