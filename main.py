from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template('/index.html', content=data)

@app.route("/add.html", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        result = dbHandler.insertContact(email, name)
        if result == True:
            return render_template("/add.html", is_done=True)
        elif result == "duplicate":
            return render_template("/add.html", is_done=False, is_duplicate=True)
        else:
            return render_template("/add.html", is_done=False, is_duplicate=False)
    else:
        return render_template("/add.html", is_done=False)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
