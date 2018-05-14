from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

cache = redis.Redis(host='redis', port=6379)

@app.route("/")
def hello():
    return jsonify("Hello World!")

@app.route("/data")
def get_data():
    return jsonify(cache.get('data'))

@app.route("/data", methods=['POST'])
def set_data():
    return request.get_json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
