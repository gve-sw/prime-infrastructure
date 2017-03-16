import requests

apiUrl = "https://198.18.134.53/webacs/api/v1/"
authToken = "Basic aWx1a2ljOjE4NjUxNw=="


def postNewTempFolder (apiUrl, authToken, folderName):
	apiNewFolderUrl = "op/cliTemplateConfiguration/folder"
	payload = {
    	'folderFQN': folderName
    }
	headers = {
    	'content-type': "application/json; charset=utf-8",
    	'authorization': authToken,
    }
	response = requests.request("POST", apiUrl + apiNewFolderUrl, data=payload, headers=headers, verify=False)
	return(response.text)


if __name__ == '__main__':
	print(postNewTempFolder(apiUrl, authToken, "Ivana"))
