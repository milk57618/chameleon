from kibeom.zero.report import Reporter
from kibeom.zero.htmonitor import Monitor

monitor = Monitor()
h,t = monitor.getHumidTemp()

reporter = Reporter()

reporter.sendData(h,t)