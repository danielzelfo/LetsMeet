from flask import Flask, request
from flask import render_template

class User:
    def __init__(self, email, password):
        self.email = email


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/successful", methods=["POST"])
def successful():
    login_user = User(request.form["email"], request.form["password"])
    print(login_user.email)
    print(login_user.password)
    return render_template("user/index.html")

@app.route("/orgLogin")
def orgLogin():
    user["email"] = request.form["email"]
    return render_template("/organizer/orgLogin.html")


@app.route("/userSignUp")
def userSignUp():
    return render_template("/user/signUp.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/orgOpenTime")
def orgOpenTime():
    return render_template("/organizer/orgOpenTime.html")    

@app.route("/orgUserInfo")
def orgUserInfo():
    return render_template("/organizer/orgUserInfo.html")  

@app.route("/logout")
def logout():
    return render_template("/logout.html")  

app.run()
