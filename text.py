from twilio.rest import Client
from keys import twilio_keys

def send_text(time):
  message = 'Leaving now. Be home in ' + str(time)
  client = Client(twilio_keys['account'], twilio_keys['token'])
  message = client.messages.create(to=twilio_keys['recipient'], from_=twilio_keys['twilio_phone'], body=message)
