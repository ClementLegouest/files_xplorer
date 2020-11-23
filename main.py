from flask import Flask
from pathlib import Path
from markupsafe import escape

app = Flask(__name__)
p = Path('/')

@app.route('/')
def hello_world():
    response = '<h1>Hello World!</h1>'
    response += '<p>Go to <a href="/files">files</a></p>'
    return response

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
    return response

@app.route('/files/<path:path>')
def infile(path):
    response = ''
    file_path = '/' + path

    response += '<h1>Dans le répertoire ' + file_path + '</h1>'
    response += '<p>Go <a href="/files">root</a></p>'
    response += get_files_list(file_path)

    return response

def get_files_list(path):
    response = ''
    p = Path(path)
    files = [x for x in p.iterdir()]

    response += '<ul>'
    for file in files:
        response += '<li>'
        filename = str(file).split('/')[len(str(file).split('/')) - 1]
        if file.is_dir():
            response += ('(d) <a href="/files' + str(file) + '">' + filename + '</a>')
        elif file.is_symlink:
            response += ('(sl) ' + filename)
        else:
            response += ('(f) ' + filename)
        response += '</li>'
    response += '</ul>'

    return str(response)