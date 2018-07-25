from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/term/<term_code>')
def schools_route(term_code):

    data = {}

    data['schools'] = get_schools(term_code)

    return render_template('schools.html',term_code=term_code, **data)
	