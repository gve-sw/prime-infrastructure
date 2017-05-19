#Prime Infrastructure

import requests

apiUrl = "https://198.18.134.53/webacs/api/v1/"
authToken = "Basic aWx1a2ljOjE4OTQ4Ng=="

def getSyslogs (apiUrl, authToken):
	apiSysUrl = "data/Syslogs.json"
	headers = {
    	'authorization': authToken
    }
	response = requests.request("GET", apiUrl + apiSysUrl, headers=headers, verify=False)
	return(response.text)

if __name__ == '__main__':
	print(getSyslogs(apiUrl, authToken))