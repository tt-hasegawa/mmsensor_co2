import logging
import mh_z19
import time
import requests


logging.basicConfig(filename='/tmp/sensor-co2.log', level=logging.DEBUG)

url='http://192.168.46.128:3000'
#proxies = {
#    'http': 'http://proxy.matsusaka.co.jp:12080',
#    'https': 'http://proxy.matsusaka.co.jp:12080'
#}
proxies = {
    'http': None,
    'https': None
}

logging.info("CO2Sensor Start.[{}]".format(url))

logging.info("CO2Sensor Initialized.")


while True:
	try:
		uploadData = mh_z19.read()
		logging.info(uploadData)
		response = requests.post(url + '/addCO2/' , json=uploadData, proxies=proxies)
	except Exception as e:
		logging.info(e)
	time.sleep(10)

