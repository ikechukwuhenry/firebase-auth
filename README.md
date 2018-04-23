# firebase-auth
Firebase auth test scripts


Working with the firebase backend especially with having phone user authentication has a 5+% failure rate.
This is high by any standard, however implementating a Phone Auth backend as implemented at Twitter, Uber etc
is easier said than done.

Below is a script for my use case of working with the firebase Python SDK. it'll be growing as I see fit.

## Auth
Authentication requires the following details in a yaml:
1.) Certificate JSON file,
2.) DB url
3.) Server key for authentication.


## Exec
```
$ git clone https://github.com/Ch3ck/firebase-auth.git
$ cd firebase-auth
$ pip install --user firebase-admin
$ python firebase-auth.py #edit file as you see fit.
```
