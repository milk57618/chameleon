from kibeom.zero.report import Reporter
import zero.htmonitor.Monitor
import zero.report.*

monitor = Monitor()
h,t = htmonitor.getHumidTemp()

reporter = Reporter()

reporter.sendData(h,t)