from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route("/login/", methods=["get", "post"])
def login():
    message = "Место порд сообщение"
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run()