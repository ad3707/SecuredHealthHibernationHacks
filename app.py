import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

from flask import Flask,request, render_template,g,Response, url_for,redirect

#Flask app variable
app = Flask(__name__)
DATABASEURI = "postgresql://aditi:350Cochran@localHost:5432/securedhealth"

engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
    try:
        g.conn = engine.connect()
    except:
        print("Cannot connect to database")
        import traceback; traceback.print_exc()
        g.conn = None

@app.teardown_request
def teardown_request(exception):
    try:
        g.conn.close()
    except Exception as e:
        pass

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def homeBack():
    return render_template("index.html")

@app.route('/availabledoctors', methods = ["GET", "POST"])
def availabledoctors():
    username = request.args.get('user')
    speciality = request.args.get('speciality')
    firstNames = []
    lastNames = []

    if len(speciality) != 0:
        try:
            cursor = g.conn.execute('SELECT D.firstName, D.lastName FROM Doctors D WHERE D.speciality = (%s)')
            for result in cursor:
                firstNames.append(result['firstName'])
                lastNames.append(result['lastName'])
            cursor.close()

            context_firstNames = dict(data_one = firstNames)
            context_lastNames = dict(data_two = lastNames)
        except Exception:
            error = 'Search failed'
    return render_template("availabledoctors", error = error, user = username, **context_firstNames, **context_lastNames)

@app.route("/confirmschedule")
def confirmschedule():
    return render_template("confirmschedule.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/schedule', methods = ["GET", "POST"])
def schedule():
    username = request.args.get('user')
    if request.method == "POST":
        speciality = request.form['speciality']

        return redirect(url_for('availabledoctors',user = username, speciality = speciality))

    return render_template("schedule.html", user = username)

@app.route("/createaccount",methods = ["GET", "POST"])
def gfg():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        Firstname = request.form.get("fname")
        Lastname = request.form.get("lname")
        DOB = request.form.get("bday")
        PhoneNumber = request.form.get("mainPhone")
        AltPhone = request.form.get("altPhone")
        Email = request.form.get("email")
        Age = request.form.get("age")
        Gender = request.form.get("gender")
        EmergFirstName = request.form.get("emergFname")
        EmergLastName = request.form.get("emergLname")
        Relationship = request.form.get("relation")
        EmergNumber = request.form.get("emergNumber")
        PharmName = request.form.get("pharmName")
        PharmNum = request.form.get("pharmNum")
        DoctorName = request.form.get("primaryName")
        DoctorNum = request.form.get("primaryNum")
        Height = request.form.get("height")
        Weight = request.form.get("weight")
        zip = request.form.get("zipcode")
        state = request.form.get("state")

        try:
            g.conn.execute('INSERT INTO Users(username,password,Firstname,Lastname,  DOB,PhoneNumber,AltPhone,Email,Age,Gender,EmergFirstName, EmergLastName, Relationship,EmergNumber,PharmName,PharmNum,DoctorName,DoctorNum,Height, Weight, streetAddress, zip, state, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%d,%s,%d,%s,%s)',username,password,Firstname,Lastname,  DOB,PhoneNumber,AltPhone,Email,Age,Gender,EmergFirstName, EmergLastName, Relationship,EmergNumber,PharmName,PharmNum,DoctorName,DoctorNum,Height, Weight, streetAddress, zip, state, city)

        except Exception:
            error = 'Invalid entry'

        if error is None:
            return redirect(url_for('dashboard',user = username))

    return render_template("createaccount.html")

@app.route("/myaccount", methods = ["GET", "POST"])
def myaccount():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        login = []
        try:
            cursor = g.conn.execute('SELECT username FROM Users WHERE username = (%s) AND password = (%s)', username, password)
            for result in cursor:
                login.append(result['username'])
            cursor.close()

        except Exception:
            error = 'Invalid search query'
        if len(login) == 1:
            return redirect(url_for('dashboard',user = username))

        error = 'Invalid username or password'

    return render_template("myaccount.html", error = error)

#start the server
if __name__ == "__main__":
	app.run()
