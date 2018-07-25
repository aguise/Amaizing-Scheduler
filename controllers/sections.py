from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/term/<term_code>/school/<schools_code>/subject/<subject_code>/catalog_num/<catalog_num>/section/<section>')
def sections_route(term_code,schools_code,subject_code,catalog_num,section):

	data = {}

	data['details'] = get_section_details(term_code,schools_code,subject_code,catalog_num,section)


	return render_template('sections.html', term_code=term_code,schools_code=schools_code, subject_code=subject_code, catalog_num=catalog_num, section=section, **data)
