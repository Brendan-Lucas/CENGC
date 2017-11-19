from twilio.rest import Client
from urllib.parse import urlencode
from urllib.request import Request, urlopen

EXPIRY_MESSAGE = "Warning: Item %s, ID %s expires in %d days.\nStorage at %s capacity."
STORAGE_MESSAGE = "Warning: Your storage is down to %d%% capacity."

api_address = "https://api.twilio.com/2010-04-01/Accounts/ACda8b10d2d90e7d392b35e11048d2b403/Messages"
twilio_sid = "ACda8b10d2d90e7d392b35e11048d2b403"
twilio_authcode = "99c1e4c804dd8579ee1b4dd5d41b1d9f"
send_to = "+16135012660"
send_from = "+13069921405"
twilio_client = Client(twilio_sid, twilio_authcode)

def expiry_alert(item, storage):
	message = twilio_client.messages.create(send_to, 
											body = EXPIRY_MESSAGE % (item["Name"], item["ID"], item["Expiry"], storage), 
											from_ = send_from)
	
	request = Request(api_address, message)

def storage_alert(percentage):
	message = twilio_client.messages.create(send_to,
											body = STORAGE_MESSAGE % percentage,
											from_ = send_from)
	
	request = Request(api_address, message)