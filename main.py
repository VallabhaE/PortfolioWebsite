import os

from flask import Flask, render_template, redirect
from flask import request
import smtplib


emailLogin = "eashwarvallabha180@gmail.com"

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
@app.route('/')
def Home(username=None,be=0):
    return render_template('index.html',e=username,c=be)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/works")
def work():
    return render_template("work.html")

@app.route("/<string:a>")
def red(a="/"):
    try:
        return render_template(a)
    except:
        return redirect("/")

@app.route("/submit",methods=["POST","GET"])
def sumbit_form():
    if request.method=="POST":
        email=request.form["email"]
        subject=request.form["subject"]
        messgae=request.form["message"]
        print(email,messgae)
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
        server.starttls()
        server.login(emailLogin,app.config['SECRET_KEY'])
        server.sendmail(emailLogin,email,"ThankYou for Giving FeedBack")
        server.sendmail(emailLogin,"ramagownieswar@karunya.edu.in","From\n"+email+"\n"+messgae)
        return redirect("/")
    return "Give Proper Resopnse"


if __name__=="__main__":
    app.run(debug=True)
