from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from app import life
from skills import imagePred

from flask_cors import CORS, cross_origin

application=Flask(__name__)
CORS(application, )
# CORS(application, supports_credentials=True)
# CORS(application, resources={r"/*": {"origins": "http://localhost:3000/"}})
# application.config['CORS_HEADERS'] = 'Content-Type', 'application/json', 'application/x-www-form-urlencoded','Access-Control-Allow-Origin'

@application.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return "Hello, World!"
    if request.method == 'POST':
        return life(request.data)

# @application.route('/guide',methods=['GET','POST'])
# def guide():
    # if request.method == 'POST':
        # return jsonify({"data":skill(request.data)}),201
@application.route('/image',methods=['POST'])
def image():
    image = request.files['image']
    print(image)
    # print()
    # return jsonify({"data":imagePred(image)}),201
    return imagePred(image)
        

if __name__=="__main__":
    application.run(debug=True ,host="0.0.0.0",port=5000)