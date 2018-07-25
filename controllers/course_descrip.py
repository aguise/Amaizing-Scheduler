from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/term/<term_code>/school/<schools_code>/subject/<subject_code>/catalog_num/<catalog_num>')
def course_descrip_route(term_code,schools_code,subject_code, catalog_num):

    data = {}

    data['course_descrips'] = get_course_description(term_code,schools_code,subject_code, catalog_num)

    data['sections'] = get_sections(term_code,schools_code,subject_code, catalog_num)
        
    return render_template('course_descrip.html', term_code=term_code,schools_code=schools_code, subject_code=subject_code, catalog_num=catalog_num, **data)