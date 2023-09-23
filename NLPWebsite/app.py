from flask import Flask,render_template,request,redirect
from database import Database
from API_handler import APIHandler

app=Flask(__name__)

database_object=Database()
api_handler=APIHandler()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=["post"])
def perform_registration():
    name=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("password")
    response=database_object.insert(name,email,password)
    if(response==1):
        message="Registration Successful! Kindly Login"
        return render_template('login.html',message=message)
    else:
        message="Email ID already exists!"
        return render_template('register.html',message=message)
    
@app.route('/perform_login',methods=["post"])
def perform_login():
    email=request.form.get("email")
    password=request.form.get("password")
    response=database_object.validate(email,password)
    if(response==0):
        return redirect('/homepage')
    elif(response==1):
        error="Incorrect password, Please try again!"
        return render_template('login.html',error=error)
    elif(response==2):
        error="Email ID doesn't exist! Please try again"
        return render_template('login.html',error=error)
    
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')

@app.route('/analyse_sentiment',methods=["post"])
def perform_sentiment_analysis():
    text=request.form.get("text")
    response=api_handler.sentiment_analysis(text)
    return render_template('sentiment_analysis.html',response=response)

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=["post"])
def perform_ner():
    text=request.form.get("text")
    response=api_handler.named_entity_recognition(text)
    return render_template('ner.html',response=response)

@app.route('/abuse_detection')
def abuse_detection():
    return render_template('abuse.html')

@app.route('/perform_abuse_detection',methods=["post"])
def perform_abuse_detection():
    text=request.form.get("text")
    response=api_handler.abuse_detection(text)
    return render_template('abuse.html',response=response)

app.run(debug=True)