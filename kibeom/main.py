from zero.report import Reporter
from zero.htmonitor import Monitor

import time

monitor = Monitor()


reporter = Reporter()

while True:
    time.sleep(15)
    h,t = monitor.getHumidTemp()
    reporter.sendData(h,t)