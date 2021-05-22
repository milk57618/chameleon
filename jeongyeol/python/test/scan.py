import threading, requests, time
from queue import Queue
def check(i,q):
    URL = "http://192.168.123.{}:5000/whoshere"
    try:
        res = requests.get(URL.format(i),timeout = 3)
        print(i,'-', res.text)
    except Exception as e:
        pass
    print(i,'fin')
threads = []
for i in range(1,256):
    time.sleep(0.33)
    a = threading.Thread(target=check, args=(i,))
    a.start()