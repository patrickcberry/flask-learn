import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>.html')
def page(path):
    print('page function')
    print(f'path: {path}')
    page = pages.get_or_404(path)
    return render_template('page.html',page=page)

app.run(host='0.0.0.0', port=5001)