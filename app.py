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

@app.route('/schedule', methods = ["GET", "POST"])
def schedule():
    username = request.args.get('user')
    if request.method == "POST":
        speciality = request.form['speciality']
        return redirect(url_for('availabledoctors',user = username,speciality = speciality))
    return render_template("schedule.html")

@app.route("/confirmschedule")
def confirmschedule():
    return render_template("confirmschedule.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")
        
@app.route("/dashboard")
def confirmation():
    return render_template("dashboard.html")

@app.route("/availabledoctors")
def availabledoctors():
    return render_template("availabledoctors.html")

@app.route("/createaccount",methods = ["GET", "POST"])
def gfg():
	if request.method == "POST":
		first_name = request.form.get("fname")
		last_name = request.form.get("lname")
		date = request.form.get("bday")
		mainNum = request.form.get("mainPhone")
		altNum = request.form.get("altPhone")
		email = request.form.get("email")
		age = request.form.get("age")
		gender = request.form.get("gender")
		emergfirst = request.form.get("emergFname")
		emerglast = request.form.get("emergLname")
		relationship = request.form.get("relation")
		emergNumber = request.form.get("emergNumber")
		pharmName = request.form.get("pharmName")
		pharmNum = request.form.get("pharmNum")
		primaryName = request.form.get("primaryName")
		primaryNum = request.form.get("primaryNum")
		weight = request.form.get("weight")
		height = request.form.get("height")
		zip = request.form.get("zipcode")
		state = request.form.get("state")
        
        try:
            g.conn.execute('INSERT INTO Users(name, breed, birthday, sex, profile_picture, bio, username, size, build) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', name, breed, birthday, sex, profile_picture, bio, username, size, build)
            
        except Exception:
            error = 'Invalid entry'
            
        if error is None:
            return redirect(url_for('dashboard',user = username))

#		return "<h1>Patient Information</h1> <br> <h5>Full Name:</h5> " +  first_name + " " + last_name  + "<br><h5>Gender: </h5>" + gender + "<br> <h5>Age:</h5> " + age + "<br> <h5>Weight: </h5>" + weight + "<br> <h5>height</h5>" + height + "<br> <h5>Primary Contact Number:</h5> " + mainNum + "<br> <h5>Alternative Phone: </h5>" + altNum + "<br><h4>Emergency Contact Info:</h4> <br> <h5>Name</h5> <br>" + emergfirst + " " + emerglast + "<br><h5>Number:</h5>" + emergNumber
	
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

