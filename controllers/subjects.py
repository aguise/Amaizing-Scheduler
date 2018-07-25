from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/term/<term_code>/school/<schools_code>')
def subjects_route(term_code,schools_code):

    data = {}

    data['subjects'] = get_subjects(term_code,schools_code)
    
    return render_template('subjects.html', term_code=term_code,schools_code=schools_code, **data)