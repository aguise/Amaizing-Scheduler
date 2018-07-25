from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/term/<term_code>/school/<schools_code>/subject/<subject_code>')
def catalog_route(term_code,schools_code,subject_code):

    data = {}

    data['catalog_nums'] = get_catalog_numbers(term_code,schools_code,subject_code)

    return render_template('catalog_num.html', term_code=term_code,schools_code=schools_code, subject_code=subject_code, **data)