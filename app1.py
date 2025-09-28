from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище данных (в реальном приложении это была бы база данных)
data_store = {
    "message": "Hello, World!",
    "items": [1,11,1,1,1]
}

@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def handle_all_methods():
    method = request.method
    print(method,'check')
    if method == 'GET':
        # Возвращаем текущее состояние данных
        return jsonify({
            "method": "GET",
            "data": data_store
        })

    elif method == 'POST':
        # Добавляем новый элемент в список items
        return jsonify({'method':'post ok'})
        

    elif method == 'PUT':
        # Полная замена данных
        return jsonify({'method':'put ok'})

    elif method == 'PATCH':
                return jsonify({'method':'patch ok'})
    elif method == 'DELETE':
        return jsonify({'method':'delete ok'})

if __name__ == '__main__':
    app.run(port=3000)