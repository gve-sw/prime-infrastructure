#Prime Infrastructure
#All five GETs from Device Details APIs

import requests

apiUrl = "https://198.18.134.53/webacs/api/v1/"
authToken = "Basic aWx1a2ljOjE4NjUxNw=="

def getAlarms(apiUrl, authToken):
	apiAlarmUrl = "data/Alarms"
	headers = {
    	'authorization': authToken
  	}
	response = requests.request("GET", apiUrl + apiAlarmUrl, headers=headers, verify=False)
	return(response.text)

def getDevices (apiUrl, authToken):
	apiDevUrl = "data/Devices"
	headers = {
    	'authorization': authToken
  	}
	response = requests.request("GET", apiUrl + apiDevUrl, headers=headers, verify=False)
	return(response.text)

def getEvents (apiUrl, authToken):
	apiEventUrl = "data/Events"
	headers = {
    	'authorization': authToken
    }
	response = requests.request("GET", apiUrl + apiEventUrl, headers=headers, verify=False)
	return(response.text)

def getSyslogs (apiUrl, authToken):
	apiSysUrl = "data/Syslogs"
	headers = {
    	'authorization': authToken
    }
	response = requests.request("GET", apiUrl + apiSysUrl, headers=headers, verify=False)
	return(response.text)

def getInventoryDetails (apiUrl, authToken):
	apiInventUrl = "data/InventoryDetails"
	headers = {
    	'authorization': authToken
    }
	response = requests.request("GET", apiUrl + apiInventUrl, headers=headers, verify=False)
	return(response.text)


if __name__ == '__main__':
	print(getAlarms(apiUrl, authToken))
	print(getDevices(apiUrl, authToken))
	print(getEvents(apiUrl, authToken))
	print(getSyslogs(apiUrl, authToken))
	print(getInventoryDetails(apiUrl, authToken))
