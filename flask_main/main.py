from flask import Flask,render_template,jsonify,request
import os
import json
from pip._vendor import requests





app = Flask(__name__)

#ip+端口+api
BACKEND_API_URL= 'http://192.168.1.108:3000/api'


@app.route('/',methods=['GET','POST'])
def root():
    return render_template('main_ui.html')


@app.route('/template_app',methods=['GET','POST'])
def input_print():

    if request.method == "POST":

        data = request.json
        x=1
        y=1
        method='add'
        print(data)
        response = requests.post(BACKEND_API_URL, json={'x':x,'y':y,'method':method})

        response=response.json()
        return jsonify(response)

    else:

        print('error')
        error_info = {"error": "print_error"}
        return jsonify(error_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
