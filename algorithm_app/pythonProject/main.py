from flask import Flask, jsonify,request
from flask_cors import CORS
from algorithm_api_numerical import add,sub,mul,div


app = Flask(__name__)
CORS(app)

@app.route('/api',methods=['GET','POST'])
def api():
    if request.method == 'POST':
        data = request.json
        print(data)
        x = float(data['x'])
        y = float(data['y'])
        method= data['method']

        print(method)
        match method:
            case 'add':
                res = add(x,y)
                return {'res':res}
            case 'sub':
                res = sub(x,y)
                return {'res':res}
            case 'mul':
                res = mul(x,y)
                return {'res':res}
            case 'div':
                res = div(x,y)
                return {'res':res}

    if  request.method == 'GET':
        return {'error':'no data input'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
