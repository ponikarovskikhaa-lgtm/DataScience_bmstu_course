from flask import Flask, render_template, request
from process import calc_cost

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def hello():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        cost = calc_cost(area)
        message = f"Стоимость квартиры: {cost} руб."
    return render_template("index.html", message=message)

@app.route("/login", methods=['post', 'get'])
@app.route("/login/", methods=['post', 'get'])
def login():
    message = "Место под сообщение"
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username != "123":
            message = "Неправильное имя пользователя"
            
        else:
            message = f"Имя пользователя: {username}, пароль {password}"
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run()