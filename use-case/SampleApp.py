#		Cisco Prime Infrastructure v 3.1
#               v.03
#
#		Hamad Alkathiri (halkathi@cisco.com)
#		Ivana Lukic (ilukic@cisco.com)
#		Haya Alzeer (halzeer@cisco.com)
#		
#		DESCRIPTION: This sample app leverages the integration of PrimeAPI 
#					 and SparkAPI to send notification to Spark based on getAlarms
#					 From Prime.
#		
#		NOTE: 		This script is for illustration purposes only. 



import PrimeApi 
import SparkAPI

if __name__ == '__main__':
	prime = PrimeApi.PrimeApi('https://198.18.134.53/webacs/api/v1','aGFsa2F0aGk6MTk3NzM0')
	result = prime.getAlarms()


