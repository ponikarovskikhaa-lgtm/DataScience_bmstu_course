from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route("/login/")
def login():
    return render_template("login.html")

#if __name__ == "__main__":
#    app.run()
app.run()