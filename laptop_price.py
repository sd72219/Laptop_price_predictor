from flask import Flask, redirect, url_for, render_template, request
import utils

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index2.html') 

@app.route('/win/<int:score>')
def win(score):
    return render_template('result.html',result=score)


@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    data = request.form
    if request.method == 'POST':
        print(f"The Linear model Laptop Price: {data}")


        x1 = float(data['Company'])
        x2 = float(data['TypeName'])
        x3 = float(data['Inches'])
        x4 = float(data['ScreenResolution'])
        x5 = float(data['Cpu'])
        x6 = float(data['Ram'])
        x7 = float(data['Memory'])
        x8 = float(data['Gpu'])
        x9 = float(data['OpSys'])
        x10 = float(data['Weight'])

        pred1 = utils.get_price(x1,x2,x3,x4, x5, x6, x7, x8, x9, x10)

        return redirect(url_for('win', score=pred1))
    else:
        return "Model Failed"

if __name__ == "__main__":
    app.run(debug=True)