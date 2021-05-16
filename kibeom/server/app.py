from flask import Flask,request
from flask_restful import Api
from functools import reduce

from proxy import *

app = Flask(__name__)
api = Api(app)

 
@app.route('/report', methods=['POST'])
def saveData():
    params = request.get_json()
    sortedkey = sorted(params.keys())
    concats = reduce(lambda x,y: x + "," + y,
                        list(map(lambda x: str(x)+":"+str(params[x]),sortedkey))
                    )           
    with open('data.txt','a') as f:
        f.write(concats+'\n')
    return {'status': concats}
    
@app.route('/whoshere', methods=['GET'])
def sendimhere():
    isworking = False
    try:
        isworking = util.testfunction()
    except Exception as e:
        with open('log','a') as f:
            f.write(str(e))
    return {'status': 'good' if isworking else 'bad'}
        
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)