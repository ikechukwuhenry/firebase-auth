#
# Firebase auth scripts
# Author: Nyah Check
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from google.oauth2 import service_account
from google.auth.transport import requests
import googleapiclient.discovery


# SERVICE_ACCOUNT_FILE = '/path/to/service.json'

# credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# sqladmin = googleapiclient.discovery.build('sqladmin', 'v1beta3', credentials=credentials)
# response = sqladmin.instances().list(project='exemplary-example-123').execute()

request = requests.Request()

# if id_info['iss'] != 'https://accounts.google.com':
#     raise ValueError('Wrong issuer.')

key = 'APyOXy0FYCpmsZHQt93L2uE1UYsWnkp6Vl6xeflrFb9tdKB9SrAp75uqyoulzU1sOvoVst8kTlfvKMBWlEE1luHfWkXqWWCPByOZGKZbs7oDTImDm9aRLIjJ1MHFQy4u9agNQQE9Laxon9EKx3BbmlER_oe8Wqa7s2KFAPafJ0zZNK1cAqe3vQWoBk8y6z4En9un_6W1GLuH-GCjbZmx2gjd9_K2ZSDGCg'
## Use sigin certificate to login to firebase server

try: 
	cred = credentials.Certificate('./firebase-account-dilmil-sandbox.json')
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

print cred.project_id, cred.service_account_email, cred.signer

# Get user info in backend server.

# Retrieve services via the auth package...
# self.data['authToken'] = self.data['firebaseUserIdToken']
try :

	# Test if proper auth tokens are passed in code
	user_info = service_account.verify_oauth2_token(key, request, 'https://dil-mil-sandbox.firebaseio.com')
	if user_info is not None
		print 'Successfully used Oauth to check user id token'
		print user_info.__str__()

	decoded_token = firebase_admin.auth.verify_id_token(id_token=key, check_revoked=True)
	uid = decoded_token['uid']
	user_profile = firebase_admin.auth.get_user(decoded_token['uid'])
	if user_profile is not None and 'email' in user_profile and profile['email'] is not None:
		print 'User Token is valid'
		print user_profile.__str__()

except firebase_admin.auth.AuthError:
	print 'User Token is invalid'
	print firebase_admin.auth.AuthError.message

except Exception, e:
	print e.__str__()


# (Receive token by HTTPS POST)
# ...

try:
    # Specify the CLIENT_ID of the app that accesses the backend:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

    # Or, if multiple clients access the backend server:
    # idinfo = id_token.verify_oauth2_token(token, requests.Request())
    # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
    #     raise ValueError('Could not verify audience.')

    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    # If auth request is from a G Suite domain:
    # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
    #     raise ValueError('Wrong hosted domain.')

    # ID token is valid. Get the user's Google Account ID from the decoded token.
    userid = idinfo['sub']
except ValueError:
    # Invalid token
    pass
