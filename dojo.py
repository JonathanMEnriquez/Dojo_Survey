from flask import Flask, redirect, render_template, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^([\w\-\.]+)@((\[([0-9]{1,3}\.){3}[0-9]{1,3}\])|(([\w\-]+\.)+)([a-zA-Z]{2,4}))$')
app = Flask(__name__)
app.secret_key = 'TopSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit_survey():
    if len(request.form['name']) < 1 or len(request.form['location']) < 1 or len(request.form['language']) < 1:
        flash('Please fill out all fields')
        return redirect('/')
    elif len(request.form['comment']) > 121:
        flash('Please keep comments to at most 120 characters')
        return redirect('/')
    else: 
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        comment = None
        if len(request.form['comment']) > 0:
            comment = request.form['comment']
    return render_template('result.html', comment = comment)
# have to pass variables back to the new page to be used or the other html page can't see it...this is an insecure way


app.run(debug=True)