from flask import render_template, flash, redirect
from flask import request
from app import app
import parseTextFile
from ClarificationResponder import ClarificationForm

#nounWordList = getListFromFile()
#verbWordList = getListFromFile()
setSize = 25

@app.route('/')
def home():
   return render_template('bingo.html',
		phraseSet=parseTextFile.getSetListFromFile('data/buzzPhrases.txt', setSize)
		bingoSet=parseTextFile.insertBlank( parseTextFile.getSetListFromFile('data/dictionary.txt', setSize) ))

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
