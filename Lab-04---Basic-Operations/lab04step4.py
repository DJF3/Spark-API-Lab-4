# coding=utf-8
import json
import requests

myToken="YOUR_PERSONAL_ACCESS_TOKEN_HERE"
myRoom="YOUR_ROOM_ID_HERE"
myEmail="AN_EMAIL_ADDRESS_HERE"
myToken="Bearer "+myToken

def post_membership(mytoken,roomid,email,Moderator=False):
	# The header is send to authenticate
	header = {'Authorization':mytoken, 'content-type':'application/json'}
	# NEW: we have to include the email address and room moderator status
	payload = {'roomId':roomid,'personEmail':email,'isModerator':Moderator}
	# NEW: we want to create something: use POST instead of GET
	# Send POST request with above header+payload. Put result in 'result'
	result = requests.post(url='https://api.ciscospark.com/v1/memberships',
						headers=header,json=payload)
	# Return POST request status: status '200' means 'succesful'.
	return str(result.status_code)


# Execute post_membership and put result in 'SparkResult'
SparkResult = post_membership(myToken, myRoom, myEmail)
# print result
print ("--- Member add response code:", SparkResult)
