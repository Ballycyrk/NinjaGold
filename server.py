from flask import Flask, session, request, render_template, redirect
app = Flask(__name__)
app.secret_key = "AineLucia"
@app.route('/')
def index():
  return render_template('index.html')
app.run(debug=True)
