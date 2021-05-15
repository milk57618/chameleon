from zero.report import Reporter
from zero.htmonitor import Monitor

monitor = Monitor()
h,t = monitor.getHumidTemp()

reporter = Reporter()

reporter.sendData(h,t)