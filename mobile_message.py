# signup on fast2sms website and use below code to send bulk mobile messages 
import requests
url = "https://www.fast2sms.com/dev/bulkV2"
payload = "sender_id=TXTIND&message=test&language=english&route=q&numbers=<mobile_number1>,<mobile_number2>"
headers = {
	'authorization': "<API_KEY>",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text, response.status_code)
