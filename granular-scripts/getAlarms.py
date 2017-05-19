#Prime Infrastructure

import requests

apiUrl = "https://198.18.134.53/webacs/api/v1/"
authToken = "Basic aWx1a2ljOjE4OTQ4Ng=="

def getAlarms(apiUrl, authToken):
	apiAlarmUrl = "data/Alarms.json"
	headers = {
    	'authorization': authToken
  	}
	response = requests.request("GET", apiUrl + apiAlarmUrl, headers=headers, verify=False)
	return(response.text)

if __name__ == '__main__':
	print(getAlarms(apiUrl, authToken))