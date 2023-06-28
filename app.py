from flask import Flask,redirect,url_for,request,render_template
import os
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text1 = request.form.get('Gluscose_data')
    text2 = request.form.get('BMI_data')
    text3 = request.form.get('Age_data')
    text4 = request.form.get('Pregnancies_data')
    # Load the model from the file
    modelload = joblib.load('filename.pkl')
    k = [[text1,text2,text3,text4]]
    df = pd.DataFrame(k, columns=['Glucose', 'BMI', 'Age','Pregnancies'])

    predict = modelload.predict(df)
    if predict == 1:
        return 'likely to develop diabetes'
    if predict == 0:
        return "Not a diabatic"

if __name__ == '__main__':
    app.run(debug=True)

