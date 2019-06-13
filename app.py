from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def func1():
	result = ""
	return render_template('index.html', result = result)

@app.route('/result', methods = ['POST', 'GET'])
def func2():
	if request.method == 'POST':
		result = request.form['Name']
		blob = TextBlob(result)
		for sentence in blob.sentences:
			result = sentence.sentiment.polarity
		return render_template('index.html', result = result)
	else:
		return render_template('index.html')	

if __name__ == '__main__':
	app.run(debug=True)	
