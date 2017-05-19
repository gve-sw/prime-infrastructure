#Prime Infrastructure


import requests

api = "https://198.18.134.53/webacs/api/v1/"
authToken = "Basic aGFsa2F0aGk6MTg5ODAyPQ"

def getJobSummary(apiUrl, authToken):
	apiUrl = "data/JobSummary.json"
	headers = {
    	'authorization': authToken
  	}
	response = requests.request("GET", api + apiUrl, headers=headers, verify=False)
	return(response.text)



if __name__ == '__main__':
	print(getJobSummary(api, authToken))
