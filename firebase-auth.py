#
# Firebase auth scripts
# Author: Nyah Check
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


try: 
	cred = credentials.Certificate('cert_file.json')
	print 'Credentials authentication success!'
	token = cred.get_access_token()
	print 'Token access success'
	default_app = firebase_admin.initialize_app(cred, {
		'databaseURL': 'db_url_link',
		'databaseAuthVariableOverride': {
		'uid': 'specify auth UID'
		}
	})
	print 'Default app init success!'
except:
	print 'Error occured on firebase auth'

#