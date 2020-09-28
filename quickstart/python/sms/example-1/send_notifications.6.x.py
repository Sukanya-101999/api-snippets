# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+919121327829",
    from_="+918919727394",
    body="Hello there!")
