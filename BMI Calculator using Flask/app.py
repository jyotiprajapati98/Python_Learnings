from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('form.html')

@app.route('/result', methods=['GET', 'POST'])
def bmi_result():
    bmi=''
    result = request.form 
    if request.method=='POST' and 'Weight' in request.form:
        weight=float(request.form.get('Weight'))
        height=float(request.form.get('Height'))
        bmi = calc_bmi(weight, height)
        return render_template("result.html",result=result,bmi=bmi)
        
def calc_bmi(w,h):
    return round((w /((h / 100) ** 2)),2)
if __name__ == '__main__':
    app.run(debug=True)
