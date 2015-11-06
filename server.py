from flask import Flask, session, request, render_template, redirect
import random
app = Flask(__name__)
app.secret_key = "AineLucia"
@app.route('/')
def index():
  try:
    session['gold']
  except:
    session['gold'] = 0
  print 'Back again'
  return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def gold():
  if request.form['place'] == 'farm':
    session['gold'] += random.randrange(10,21)
  elif request.form['place'] == 'cave':
    session['gold'] += random.randrange(5,11)
  elif request.form['place'] == 'house':
    session['gold'] += random.randrange(2,6)
  else:
    session['gold'] += random.randrange(-50,51)
  return render_template('index.html')
app.run(debug=True)
