from flask import Flask, render_template, abort
from pathlib import Path
from markupsafe import escape
 
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/files')
def files():
    
    response = ''
    p = Path('/')
    files = [x for x in p.iterdir() if x.is_dir()]
    response += '<h1>La racine du système</h1>'
    response += '<ul>'
    for file in files:
        if file.is_dir():
            response += ('<li><a href="/files' + str(file) + '">' + str(file) + '</a></li>')
    response += '</ul>'
    
    return render_template('files.html', files=files, path=p)