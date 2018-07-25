from flask import render_template, request
from app import app
from backpack import *

@app.route('/backpack')
def backpack_route():
	
	return render_template('backpack.html')