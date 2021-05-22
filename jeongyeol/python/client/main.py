from zero.report import Reporter
from zero.htmonitor import Monitor

import time

monitor = Monitor()
reporter = Reporter()

time.sleep(1)
while True:
    h,t = monitor.getHumidTemp()
    reporter.sendData(h,t)
    time.sleep(15)