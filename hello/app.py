import json
import ast
from flask import Flask, request
from types import SimpleNamespace
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, Welcome to the simple reservation management app!"

if __name__ == "__main__":
    app.run()