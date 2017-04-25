#      Integration of Cisco Prime Infrastructure API Wrapper & Spark API Wrapper
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


from api_spark_integrated import SparkApi

if __name__ == '__main__':

	header = SparkApi.setHeaders()
	message = SparkApi.getToken()
	result = SparkApi.postMsg(header,message)
	
