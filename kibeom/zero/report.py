import requests, json
from datetime import datetime


class Reporter():
    def sendData(self,h,t):
        data = {'humid': h, 
                'temp': t 
                }

        now = datetime.now()
        formattedDate = now.strftime("%Y%m%d_%H%M%S")

        data['time'] = formattedDate

        URL = 'http://luvbeenhere.com:5000/report'
        res = requests.post(URL, data=json.dumps(data), headers={"Content-Type":"application/json"})

        print(res.text)

