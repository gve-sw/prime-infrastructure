import requests
import base64


class PrimeApi(object):
	
	def __init__(self, server,key):
		self.server = server
		self.headers = PrimeApi.set_headers(key)

	def set_headers(key):
		accessToken_hdr = 'Basic ' + key
		prime_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
		return (prime_header)

	def getWLCDetails(self):
	    url = self.server+"/data/WlanControllerDetails.json"
	    response = requests.request("GET", url, headers=self.headers , verify=False)
	    print('HERE')
	    return (response.text)

	def getJobSummary(self):
		url = "data/JobSummary.json"
		response = requests.request("GET", url, headers=self.headers , verify=False)
		return(response.text)

	def getJobSummary(self):
		url = "op/info/uptime.json"
		response = requests.request("GET", url, headers=self.headers , verify=False)
		return(response.text)




