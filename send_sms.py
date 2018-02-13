
#from twilio.rest import Client

from twilio import rest

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="Own phone no",
    from_="twilio account",
    body="Hello from Python!")

print(message.sid)