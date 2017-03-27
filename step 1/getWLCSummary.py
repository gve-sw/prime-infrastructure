#Prime Infrastructure


import requests

api = "https://198.18.134.53/webacs/api/v1/"
authToken = "Basic aGFsa2F0aGk6MTg5ODAyPQlc"

def getWLCDetails(apiUrl, authToken):
	apiUrl = "data/WlanController.json"
	headers = {
      'content-type': "application/json",
    'authorization': "Basic aGFsa2F0aGk6MTg5ODAyPQ",
    'cache-control': "no-cache",
  	}
	response = requests.request("GET", api + apiUrl, headers=headers, verify=False)
	return(response.text)



if __name__ == '__main__':
	print(getWLCDetails(api, authToken))