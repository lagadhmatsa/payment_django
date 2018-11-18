# import os
# from twilio.rest import Client
#
#
# account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
#
# client = Client(account_sid, auth_token)
#
# client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
#                       to=os.environ.get('CELL_PHONE_NUMBER'),
#                       body='You just sent an SMS from Python using Twilio!')
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe24048a852b18d18ac49658450803864"
# Your Auth Token from twilio.com/console
auth_token  = "7f7afc0c7b5a8e3b39b82d374af486a4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917842149220",
    from_="+18649900776",
    body="Hello from Python!")

print(message.sid)