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
  try:
    session['activity']
  except:
    session['activity'] = []
  return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def gold():
  if request.form['place'] == 'farm':
    result = random.randrange(10,21)
  elif request.form['place'] == 'cave':
    result = random.randrange(5,11)
  elif request.form['place'] == 'house':
    result = random.randrange(2,6)
  else:
    result = random.randrange(-50,51)
  session['gold'] += result

  if result >= 0:
    temp = 'win'
    mess = 'You ' + str(abs(result)) + ' gold from the ' + request.form['place'] + '! '
  else:
    temp = 'lose'
    mess = 'Entered a casino and lost ' + str(abs(result)) + ' gold... will you never learn? '
  result = temp, mess
  session['activity'].append(result)
  print mess
  print session['activity']
  print result
  print temp
  return redirect ('/')
app.run(debug=True)
