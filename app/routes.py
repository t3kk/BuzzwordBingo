from flask import render_template
from app import app
from ClarificationResponder import clarify
from parseTextFile import getListFromFile

@app.route('/')
def home():
   return render_template('index.html', dict=getListFromFile('data/dictionary.txt'))

@app.route('/clarify')
def clarifyRender():
	return render_template('clarify.html')

@app.route('/bandon')
def bandon():
	return 'Bandon was here!'
