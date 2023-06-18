from flask import Flask,render_template,request,redirect,url_for
from jinja2.exceptions import TemplateNotFound
from dotenv import load_dotenv
import joblib

# female-0
# male-1
# other-3

# standers scale z=(X-2.786749e-16)/1.000005e+00

load_dotenv()

app=Flask(__name__)

@app.route("/",methods=['GET'])
def Index():
#     feature names ['gender' 'age' 'hypertension' 'heart_disease' 'smoking_history' 'bmi'
#  'HbA1c_level' 'blood_glucose_level']

    try:
        return render_template("index.html",title="Home")
    except TemplateNotFound:
        return "template not found"
    

@app.route('/predict',methods=['POST'])
def predict():
    
    data=request.form
    model=joblib.load('../model.joblib')

    try:
        gender=int(data.get('gender'))
        age=int(data.get('age'))
        bmi=float(data.get('bmi'))
        hypertension=int(data.get('hypertension'))
        heart_disease=int(data.get('hd'))
        smoking_history=int(data.get('smoke'))
        HbA1c_level=float(data.get('HbA1c_level'))
        bgl=float(data.get('bgl'))

    except Exception:
        return redirect('/')

    if not gender in [0,1,2]:
        return redirect('/')
    if not smoking_history in range(6):
        return redirect('/')

    std_gl=(bgl-2.786749e-16)/1.000005e+00
    #['gender' 'age' 'hypertension' 'heart_disease' 'smoking_history' 'bmi'
#  'HbA1c_level' 'blood_glucose_level']

    ans=model.predict([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,std_gl]])

    # return [gender,age,bmi,hypertension,heart_disease,smoking_history,HbA1c_level,bgl,std_gl]

    return redirect(url_for('Results',results=ans[0]))

@app.route("/results",methods=['GET'])
def Results():
    res=request.args['results']
    return render_template('result.html',results=res)