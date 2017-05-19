#      Cisco Prime Infrastructure v 3.1
#               v.03
#
#      Hamad Alkathiri (halkathi@cisco.com)
#      Ivana Lukic (ilukic@cisco.com)
#      Haya Alzeer (imarifin@cisco.com)
#              Apr 2017
#             
#              This class provides methods to facilitates
#              access to the Advanced Malware Protection API.
#
#   REQUIREMENTS:
#              Python sys library
#              AMP Wrapper_API module to access the AMP API
#
#   WARNING:
#              This script is meant for educational purposes only.
#              Any use of these scripts and tools is at
#              our own risk. There is no guarantee that
#              they have been through thorough testing in a
#              comparable environment and we are not
#              responsible for any damage or data loss
#              incurred with their use.
#
#   INFORMATION:
#              If you have further questions about this API and script, please contact GVE. Here are the contact details:
#                              For internal Cisco employees, please contact GVE at http://go2.cisco.com/gve
#                              For Cisco partners, please open a case at www.cisco.com/go/ph
 


import requests
import json
from SparkAPI import SparkAPI

class PrimeApi(object):
	
	#intiating the class instance
	def __init__(self, server,key):
		self.server = server
		self.headers = PrimeApi.set_headers(key)

	#Setting headers for HTTP Call
	def set_headers(key):
		accessToken_hdr = 'Basic ' + key
		prime_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
		return (prime_header)
		
	#getting all critical alarms at once as entities list
	def getAlarms(self):
		url = self.server+ "/data/Alarms.json?"
		#setting alarm severity level 
		severityLevel= "severity=CRITICAL&acknowledgementStatus=False"
		url = url + severityLevel
		response = requests.request("GET", url, headers=self.headers , verify=False)
		jsonResponse = json.loads(response.text)
		#will iterate through alarms and pick alarm IDs
		for id in jsonResponse['queryResponse']['entityId']:
			value = id['$']
			self.getAlarmsById(value)

	#get alarm by id to get more info 
	def getAlarmsById(self,id):
		url = self.server+ "/data/Alarms/"+id+".json"
		response = requests.request("GET", url, headers=self.headers , verify=False)
		alarmJsonResponse = json.loads(response.text)
		#print ("###############################")
		
		#sends messages to spark
		for alarm in alarmJsonResponse['queryResponse']['entity']:
			self.sendToSpark('AlarmID:'+str(alarm['alarmsDTO']['alarmId'])+ "\n Time: "+ alarm['alarmsDTO']['timeStamp'] + "\n Message: "+ alarm['alarmsDTO']['message']+ "\n Link: "+alarm['@url'] + "\n\n")
			#self.sendToSpark()
			#self.sendToSpark('Time: '+)
			#self.sendToSpark()
			#self.sendToSpark('Message: '+)
			#self.sendToSpark()
			#self.sendToSpark('Link: ' +)

	#Sends alarm messages to Spark
	def sendToSpark(self,sparkMessage):
		sparkHeader = SparkAPI.setHeaders()
		#sparkMessage = SparkAPI.getToken()
		result = SparkAPI.postMsg(sparkHeader,sparkMessage)

	def getWLCDetails(self):
	    url = self.server+"/data/WlanControllerDetails.json"
	    response = requests.request("GET", url, headers=self.headers , verify=False)
	    return (response.text)

	def getJobSummary(self):
		url = self.server+"/data/JobSummary.json"
		response = requests.request("GET", url, headers=self.headers , verify=False)
		return(response.text)

	def getSystemUptime(self):
		url = self.server+ "/op/info/uptime.json"
		response = requests.request("GET", url, headers=self.headers , verify=False)
		return(response.text)


		





