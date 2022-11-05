from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import base64
import os
import json
import tensorflow as tf
from tensorflow import keras

md = tf.keras.models.load_model("bestmodel.h5")

app = Flask(__name__)
CORS(app, headers=['Content-Type'])

@app.route("/", methods=["POST", "GET", 'OPTIONS'])
def index_page():
	return render_template('index.html')


@app.route('/hook2', methods = ["GET", "POST", 'OPTIONS'])
def predict():
    return "<h1>trial</h1>"
    
    
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=False)