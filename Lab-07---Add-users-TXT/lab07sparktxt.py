# coding=utf-8
import json
import requests
import sys

myToken="YOUR_PERSONAL_ACCESS_TOKEN_HERE"

# check the length of the argument. Not enough?: Print message
argLen = len(sys.argv)
if argLen < 3 :
	print("Usage: "+sys.argv[0]+" <email file> <room title>")
	exit(0)
# Put arguments in variable so it can be used later
emailFile = sys.argv[1]   # first argument
roomTitle = sys.argv[2]	  # second argument
# Read the email file and save the emails in an list
emails = [line.strip() for line in open(emailFile)]

# Define header used for authentication
headers = { "Authorization": "Bearer "+myToken,
			"Content-type": "application/json" }

# Define the action to be taken in the HTTP request
roomInfo = { "title": roomTitle }

# Execute HTTP POST request to create the Spark Room
r = requests.post("https://api.ciscospark.com/v1/rooms",headers=headers, json=roomInfo)
room = r.json()
# Print the result of the HTTP POST request
print(room)


for email in emails:
	# if it's an blank line don't add:
	if email=="": continue
	# Set the HTTP request payload (action)
	membershipInfo = { "roomId": room["id"],
		"personEmail": email }
	# Execute HTTP POST request to create the Spark Room
	r=requests.post("https://api.ciscospark.com/v1/memberships",
		headers=headers, json=membershipInfo)
	membership = r.json()
	print(membership)
	print()
