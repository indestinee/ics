from flask import Flask, render_template, redirect, url_for
import os
from ics import *
from config import cfg

app = Flask(__name__, static_folder='templates', static_url_path='')
app.config['SECRET_KEY'] = 'AKALFHUEWSAiowqjodas'  

def get_ics():
    params = cfg.params

    for index, param in enumerate(params):
        ics = generate(**param)
        h = hex(hash(ics))[2:]
        path = 'ics/{}:{}.ics'.format(index, h)
        with open(os.path.join('templates', path), 'w') as f:
            f.write(ics)
        param['path'] = path
    return params
        

@app.route("/")
def index(): 
    html_items = {
        'template_name_or_list': 'index.html',
        'icss': get_ics(),
    }
    return render_template(**html_items)

os.system('rm ./templates/ics/*ics')

port = 1235
app.run(host='::', port=port, debug=True)
