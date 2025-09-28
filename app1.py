from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Главная страница с формами для тестирования
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Единая точка для тестирования всех методов
@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test_methods():
    if request.method == 'GET':
        # Просто отображаем форму (уже сделано на index.html)
        return jsonify({"message": "GET запрос получен", "method": "GET"})

    elif request.method == 'POST':
        data = request.form.to_dict() or request.get_json() or {}
        return jsonify({
            "message": "POST запрос получен",
            "method": "POST",
            "data": data
        })

    elif request.method == 'PUT':
        data = request.get_json() or {}
        return jsonify({
            "message": "PUT запрос получен",
            "method": "PUT",
            "data": data
        })

    elif request.method == 'DELETE':
        return jsonify({
            "message": "DELETE запрос получен",
            "method": "DELETE"
        })

if __name__ == '__main__':
    app.run(debug=True)