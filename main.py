from flask import Flask, render_template, request, redirect
from pathlib import Path

app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.errorhandler(405)
def method_not_allowed(error):
  return redirect("/")

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
  filename = request.args.get('filename')
  if request.method == 'POST':
    text = request.form['text']
    with open(filename, 'w') as file:
      file.write(text)
    return redirect("/blank")
    
  elif request.method == 'GET':
    file = Path(filename)
    if file.is_file():
      with open(filename, 'r') as file:
        text = file.read()
    else:
      with open(filename, "w") as file:
        file.write("")
        text = ""
    return render_template('edit.html', filename=filename, text=text)

@app.route("/blank")
def blank():
  return ('', 204)
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
