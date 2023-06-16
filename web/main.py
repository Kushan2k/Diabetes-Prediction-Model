from flask import Flask,render_template
from jinja2.exceptions import TemplateNotFound
from dotenv import load_dotenv


load_dotenv()

app=Flask(__name__)

@app.route("/")
def Index():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        return "template not found"


if __name__=='__main__':
    app.run()