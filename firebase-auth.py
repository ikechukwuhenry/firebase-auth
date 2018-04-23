#
# Firebase auth scripts
# Author: Nyah Check
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('./authKey.json')
cred = credentials.RefreshToken('path/to/refreshToken.json')
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL': '',
	'databaseAuthVariableOverride': {
		'uid': 'service-worker'
	}
})

firebase_admin.initialize_app(cred, {
				'databaseURL': self.config.get('firebase', 'db_url'),
				'databaseAuthVariableOverride': {
					'uid': 'service-worker'
				}
			})