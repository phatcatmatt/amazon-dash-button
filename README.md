A python3 script to detect an amazon dash button press and send a text message containing an arrival time. Uses google maps distance matrix to calculate travel time between two locations and twilio to send the text. Works with the newer Dash Button model JK29LP. 

1. `pip3 install scapy-python3 googlemaps twilio`
2. might need to `apt-get install tcpdump`
3. `touch keys.py`
4. Add your API keys to keys.py like so:
`maps_key = 'XXXXX'
twilio_keys = {
'account : 'XXXXX'
'token' : 'XXXXX'
'recipient' : '+12345678900' # recipient's phone number formatted like so
'twilio_phone' : '+19876543210'# the phone number twilio gives you
}` 
4. `python3 detect-button.py` 
