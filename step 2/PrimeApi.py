import requests
import requests.packages.urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth # for Basic Auth
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # Disable insecure https warnings


class PrimeApi:
	
	def __init__(self, server, key):
		self.server = server
		self.headers = PrimeApi.set_headers(key)

	def set_headers(key):
		accessToken_hdr = 'Bearer ' + key
		prime_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
		return (prime_header)

	def getWLCDetails():
	    url = self.server+"/data/WlanControllerDetails.json"
	    response = requests.request("GET", url, headers=self.headers)
	    return (response.text)

	def getJobSummary():
		url = "data/JobSummary.json"
		response = requests.request("GET", url, headers=self.headers)
		return(response.text)

	def getJobSummary():
		url = "op/info/uptime.json"
		response = requests.request("GET", url, headers=self.headers)
		return(response.text)
		





