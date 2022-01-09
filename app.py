from flask import Flask,request, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
	return render_template("index.html")
 
@app.route("/home")
def homeBack():
    return render_template("index.html")

@app.route("/schedule")
def schedule():
        return render_template("schedule.html")

@app.route("/confirmschedule")
def confirmschedule():
        return render_template("confirmschedule.html")

@app.route("/confirmation")
def confirmation():
        return render_template("confirmation.html")

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

		return "<h1>Patient Information</h1> <br> <h5>Full Name:</h5> " +  first_name + " " + last_name  + "<br><h5>Gender: </h5>" + gender + "<br> <h5>Age:</h5> " + age + "<br> <h5>Weight: </h5>" + weight + "<br> <h5>height</h5>" + height + "<br> <h5>Primary Contact Number:</h5> " + mainNum + "<br> <h5>Alternative Phone: </h5>" + altNum + "<br><h4>Emergency Contact Info:</h4> <br> <h5>Name</h5> <br>" + emergfirst + " " + emerglast + "<br><h5>Number:</h5>" + emergNumber
	return render_template("createaccount.html")

@app.route("/myaccount", methods = ["GET", "POST"])
def myaccount():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		return "<h1>Patient Information</h1>"
	return render_template("myaccount.html")

#start the server
if __name__ == "__main__":
	app.run()

