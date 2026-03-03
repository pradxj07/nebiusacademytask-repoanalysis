from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  # home endpoint
    return "<h1>GitHub Repository Analysis API</h1>"



if __name__ == '__main__':
    app.run(host='127.0.0.0', port=5000)