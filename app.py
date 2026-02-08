from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for users
users = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        print("method call",request.form)
        username = request.form["username"]
        password = request.form["password"]

        users[username] = password   
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in users and users[username] == password:
            return f"Welcome {username}! Login Successful"
        else:
            return "Invalid Username or Password"

    return render_template("login.html")

app.run(debug=True)