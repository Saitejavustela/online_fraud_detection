from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
model = pickle.load(open('payments.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def about():
    return render_template('home.html')
@app.route('/home')
def about1():
    return render_template('home.html')

@app.route('/predict')
def home1():
    return render_template('predict.html')

@app.route('/pred',methods=['POST','GET'])
def predict():
    x=[[x for x in request.form.values()]]
    print(x)

    x=np.array(x)
    print(x.shape)

    print(x)
    pred=model.predict(x)
    print(pred[0])
    result = "is Fraud" if pred[0] == 1 else "Not Fraud"
    return render_template('submit.html',prediction_text=result)

if __name__=='__main__':
    app.run(debug=False)