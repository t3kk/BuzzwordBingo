from flask import render_template
from app import app
from ClarificationResponder import clarify

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/clarify')
def clarifyRender():
	return render_template('clarify.html')

@app.route('/bandon')
def bandon():
	return 'Bandon was here!'
