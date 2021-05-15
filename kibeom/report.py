import requests, json
def sendData(h,t):
    data = {'humid': h, 
            'temp': t , 
            'time': '2021051623123232'}
    URL = 'http://luvbeenhere.com:5000/report'
    res = requests.post(URL, data=json.dumps(data), headers={"Content-Type":"application/json"})
    print(res.text)

sendData(1,2)

