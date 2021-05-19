import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
POS = "TH01"

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
f=open('temp_log.txt', 'a')
if humidity is not None and temperature is not None:
    print("{0},{1},{2},{3:0.1f},{4:0.1f}".format(POS, time.strftime('%y/%m/%d'), \
                             time.strftime('%H:%M:%S'), temperature, humidity))
    f.write("{0},{1},{2},{3:0.1f},{4:0.1f}\n".format(POS, time.strftime('%y/%m/%d'), \
                                 time.strftime('%H:%M:%S'), temperature, humidity))
else:
    print("{0},{1},{2}, Data Error".format(POS, time.strftime('%y/%m/%d'), \
                                              time.strftime('%H:%M:%S')))
    f.write("{0},{1},{2}, Data Error\n".format(POS, time.strftime('%y/%m/%d'), \
                                                  time.strftime('%H:%M:%S')))
f.close()

