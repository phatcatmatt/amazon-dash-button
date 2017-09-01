A python 3 script to detect an Amazon Dash Button press and send a text message containing an arrival time. Uses Google Maps distance matrix to calculate travel time between two locations and Twilio to send the text. Works with the newer Dash Button model JK29LP.

#### Steps

1. `pip3 install scapy-python3 googlemaps twilio`
2. `touch keys.py`
3. Add your API keys to keys.py like so:
```python
maps_key = 'XXXXX'
twilio_keys = {
'account' : 'XXXXX',
'token' : 'XXXXX',
'recipient' : '+12345678900', # recipient's phone number formatted like so
'twilio_phone' : '+19876543210', # the phone number twilio gives you
}
``` 
4. `python3 detect-button.py`
5. Press the button!

##### Notes
You'll likely need to run the script as root. You also might need to `apt-get install tcpdump`. On a Raspberry Pi I had to update some existing packages to fix some conflicts.
