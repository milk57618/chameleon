import requests, json
def sendData(h,t):
    data = {'humid': h, 
            'temp': t , 
            'time': '2021051623123232'}
    URL = 'luvbeenhere.com/report'
    res = requests.post(URL, data=json.dumps(data))

