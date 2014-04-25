from flask import render_template, flash, redirect
from flask import request
from app import app
from parseTextFile import getSetFromFile
from ClarificationResponder import ClarificationForm

setSize = 25

@app.route('/')
def home():
   return render_template('index.html', bingoSet=getSetFromFile('data/dictionary.txt', setSize))

@app.route('/clarify', methods = ['GET', 'POST'])
def clarify():
	form = ClarificationForm()
	if form.validate_on_submit():
		flash('Clarification Response to ' + form.clarificationText.data)
		return redirect('/clarify')
	return render_template('clarify.html', title = 'Clarifications', form = form)

@app.route('/bandon')
def bandon():
	return 'Bandon was here!'
