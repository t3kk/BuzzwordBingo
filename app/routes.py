from flask import render_template
from app import app
from ClarificationResponder import clarify
from parseTextFile import getSetFromFile

tableSize = 5

@app.route('/')
def home():
   return render_template('index.html', bingoSet=getSetFromFile('data/dictionary.txt', tableSize*tableSize), tableSize=tableSize)

@app.route('/clarify')
def clarifyRender():
	return render_template('clarify.html')

@app.route('/bandon')
def bandon():
	return 'Bandon was here!'
