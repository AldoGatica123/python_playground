from os import environ

FROM_ADDR = environ.get('FROM_ADDR')
PASSWORD = environ.get('PASSWORD')
TO_ADDR = environ.get('TO_ADDR')

ACCOUNT_SID = environ.get('ACCOUNT_SID')
AUTH_TOKEN = environ.get('AUTH_TOKEN')
FROM_NUMBER = environ.get('FROM_NUMBER')
MY_NUMBER = environ.get('MY_NUMBER')
SERVICE_SID = environ.get('SERVICE_SID')