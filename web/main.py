from flask import Flask,render_template
from jinja2.exceptions import TemplateNotFound
from dotenv import load_dotenv
import joblib


load_dotenv()

app=Flask(__name__)
model=joblib.load('../model.joblib')

@app.route("/")
def Index():
#     feature names ['gender' 'age' 'hypertension' 'heart_disease' 'smoking_history' 'bmi'
#  'HbA1c_level' 'blood_glucose_level']

    try:
        return render_template("index.html",title="Home")
    except TemplateNotFound:
        return "template not found"
