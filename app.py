from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('base.html')

@app.route('/marksheet',methods = ['POST', 'GET'])
def marksheet():
    if request.method == 'POST':
        marksheet = request.form
        return render_template("marks.html", marksheet = marksheet)


if __name__ == '__main__':
    app.run(debug = True)
