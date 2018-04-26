#
# Firebase auth scripts
# Author: Nyah Check
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import json

uid = 'QKBODoCx76hZS1jyWFAnMQRtGwv2' # user with phone number
firebaseAppId = 'dil-mil-sandbox'
key = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjMwNDZhMTU2MzczNjZiNGQ2NGQ5YTVhYmIzMzczMTgyYmE0ZDdjZmIifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZGlsLW1pbC1zYW5kYm94IiwiYXVkIjoiZGlsLW1pbC1zYW5kYm94IiwiYXV0aF90aW1lIjoxNTI0Njk2NDE5LCJ1c2VyX2lkIjoiYTNHSVJJdGZBbWhtNGVqaFBFc2NHcEZwNjBoMSIsInN1YiI6ImEzR0lSSXRmQW1obTRlamhQRXNjR3BGcDYwaDEiLCJpYXQiOjE1MjQ2OTY0OTcsImV4cCI6MTUyNDcwMDA5NywicGhvbmVfbnVtYmVyIjoiKzE0MjQzNzE0NjEwIiwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJwaG9uZSI6WyIrMTQyNDM3MTQ2MTAiXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwaG9uZSJ9fQ.k98jQINvRfsuNzLwae1LJvaReIlMPxHkP_0tM5Eq1UGJhSF-9et9jru1ffdj0ewGOkCeOu3bgjhTCBuwvimyVx0pyosvF29zfcn52PJCYar0aXevIjRRcSTYDM5p0K4lY4QGK-WAzJpKPrd3ra9MbDp2LlgvW9OG7ylbCC9PDRlchuFLO-7M-aTtaKmXhWdn9EJBI1A4XnQR8NlMDGEiWYv0EB3xoNhuwpi-lTgkk9c7r1BSZhPDqgMDpJbfuo3F09oA2f26GmQBB3dHVXORNPdHY0KSH8pXKsVhF_H-gcOJWVWHhyn1O-Lwm7GhVrfEvFbC3OVQKWLm023okA7vDw'


try: 
	cred = credentials.Certificate('./credCertificate.json')
	print 'Credentials authentication success!'
	token = cred.get_access_token()
	print 'Token access success'
	default_app = firebase_admin.initialize_app(cred, {
		'databaseURL': 'https://dil-mil-sandbox.firebaseio.com',
		'databaseAuthVariableOverride': {
		'uid': 'service-worker'
		}
	})
	print 'Default app init success!'
except:
	print 'Error occured on firebase auth'

# print cred.project_id, cred.service_account_email, cred.signer

# Get user info in backend server.

# Retrieve services via the auth package...

# Test if proper auth tokens are passed in code
#try:
	
	# print custom_token

	# # Verifies an ID Token issued by Firebase Authentication.
	# token = firebase_admin.auth.verify_id_token(key)
	# uid = token['uid']
	# #token = id_token.verify_firebase_token(key, request, audience=firebaseAppId)
	# print 'Verify firebase Token', uid
	# print token
	# Get user info
	# user_info = id_token.verify_oauth2_token(key, request, audience=firebaseAppId)
	# if user_info is not None:
	# 	userid = user_info['sub']
	# 	print 'Successfully used Oauth to check user id token'
	# 	print user_info.__str__(), userid

# except Exception, e:
# 	print e.__str__()

try :

	# #create custom token with uid
	# custom_token = firebase_admin.auth.create_custom_token(uid)
	# print 'KEY: ', custom_token
	decoded_token = firebase_admin.auth.verify_id_token(key)
	print 'Decoded Token:  '
	print decoded_token
	new_uid = decoded_token['uid']
	print 'UID: '
	print uid
	user_profile = firebase_admin.auth.get_user(new_uid)
	print json.dumps(user_profile)
	if user_profile is not None:
		print 'User Token is valid'
		print user_profile.display_name, user_profile.email, user_profile.phone_number, user_profile.photo_url

except firebase_admin.auth.AuthError, err:
	print 'User Token is invalid'
	print err.message

except Exception, e:
	print e.__str__()
