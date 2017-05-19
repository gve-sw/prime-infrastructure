#      Cisco Spark API Wrapper
#               v.02
#
#      Hamad Alkathiri (halkathi@cisco.com)
#      Haya Alzeer (halzeer@cisco.com)
#      Ivana Lukic (ilukic@cisco.com)
#              April 2017
#
#              This class provides methods to facilitate
#              the use of the Spark API.
#
#   SPECIAL THANKS:
#              Thanks to the ase-apj-team-charlie, for allowing us to reuse and modify the Spark scripts. 
#
#   REQUIREMENTS:
#              Python requests library (python-requests)
#              Json library
#              readSettings library, for obraining tokens from a file
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

import json
import requests
import readSettings


class SparkApi(object):
	
	global token
	global roomId

	def __init__(self):
		self.headers = SparkApi.setHeaders()

	#Getting Bot token from a file
	def getBotToken():
		appSettings = readSettings.loadSettings("settings.txt")
		botToken = appSettings[1].rstrip()
		return botToken
	
	def getToken():
		appSettings = readSettings.loadSettings("settings.txt")
		bot = appSettings[2].rstrip()
		return bot

	token = getBotToken()

	#Sets the header to be used for authentication and data format to be sent.
	def setHeaders():
		accessToken_hdr = 'Bearer ' + token
		spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
		return (spark_header)

	'''
	# creates a new room and returns the room id.
	def createRoom(the_header,room_name):
		roomInfo = '{"title":"' + room_name + '"}'
		uri = 'https://api.ciscospark.com/v1/rooms'
		resp = requests.post(uri, data=roomInfo, headers=the_header)
		var = resp.json()
		print("createRoom JSON: ", var)
		return var ["id"]
	'''
	
	#Getting Room ID from a file
	def getRoomId():
		appSettings = readSettings.loadSettings("settings.txt")
		roomID = appSettings[0].rstrip()
		return roomID

	roomId = getRoomId()

	#Posts a message to the room
	def postMsg(the_header,message):
		message = {"roomId":roomId,"text":message}
		uri = 'https://api.ciscospark.com/v1/messages'
		resp = requests.post(uri, json=message, headers=the_header)
		print("postMsg JSON: ", resp.json())





