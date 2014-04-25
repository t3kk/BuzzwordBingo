from flask import render_template
from app import app
import parseTextFile

#nounWordList = getListFromFile()
#verbWordList = getListFromFile()
setSize = 25

@app.route('/')
def home():
   return render_template('index.html',
     bingoSet=parseTextFile.insertBlank( parseTextFile.getSetListFromFile('data/dictionary.txt', setSize) ))

@app.route('/clarify')
def clarify():
	return render_template('clarify.html')

@app.route('/bandon')
def bandon():
	return 'Bandon was here!'
