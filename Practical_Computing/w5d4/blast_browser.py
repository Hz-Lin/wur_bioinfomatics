#!/usr/bin/env python

from db_functions import get_targets, get_rows_for_target
from flask import Flask, request, render_template

# create web application
app = Flask(__name__)

@app.route('/')
def index():
    targets_list = get_targets()
    return render_template('index.html',targets=targets_list)

@app.route('/results')
def show_results():
    target = request.args['target']
    evalue = float(request.args['cutoff'])
    blast_results = get_rows_for_target(target,evalue)
    return render_template('results.html',rows=blast_results)

if __name__ == "__main__":
    # start the web application
    app.run()
