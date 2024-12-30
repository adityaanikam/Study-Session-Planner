from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for sessions
sessions = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    global sessions
    if request.method == "POST":
        goal = request.form["goal"]
        time = request.form["time"]
        technique = request.form["technique"]
        sessions.append({"goal": goal, "time": time, "technique": technique})
    return render_template("dashboard.html", sessions=sessions)

if __name__ == "__main__":
    app.run(debug=True)
