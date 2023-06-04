from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE'])
def index():
    return render_template('index.html')

@app.route('/info', methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE'])
def handle_info_request():
    try:
        method = request.method
        url = request.url
    except Exception as e:
        pass

    data = ''
    
    try:
        data = request.form.get('data')

    except Exception as e:
        pass

    # TODO: 해당 메서드에 따른 패킷 처리 로직 구현

    header_info = f"{method} {url}\n{request.headers}"

    response = {
        'headerInfo': header_info,
        'data': data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
