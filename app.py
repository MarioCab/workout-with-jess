import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("LIVE_SID")
auth_token = os.getenv("LIVE_AUTH")
client = Client(account_sid, auth_token)



message = client.messages.create(
    to="+15169418868", 
    messaging_service_sid=os.getenv("MSG_SID"),
    body="Hello from Python!")

#print(message.sid)


print (message)