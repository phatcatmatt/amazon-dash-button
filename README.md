A python 3 script to detect an Amazon Dash Button press and send a text message containing an arrival time. Uses Google Maps distance matrix to calculate travel time between two locations and Twilio to send the text. Works with the newer Dash Button model JK29LP.

### Steps

#### Find the MAC address

1. Press and hold the Dash Button for about 5 seconds (the light will pulse blue)
2. Connect to the SSID 'Amazon ConfigureMe' with any device
3. Navigate to http://192.168.0.1 and copy down the MAC address

#### Set up the Dash Button

1. Install the Amazon app on any device
2. Open the app and go to Your Account > Dash Buttons & Devices
3. Follow the instructions to connect the button to your network
4. Don't select a product for the button, just quit the app

Now if you press the button it will connect to the network but since you haven't selected a product it won't order anything. You will get a notification on your device every time you press the button prompting you to finish setting up your button. If you really hate this you can go into your router and blacklist the buttons MAC address so that it never actually connects to the internet, thereby preventing notifications being triggered.

#### Set up your Raspberry Pi

1. Connect your pi to the router via ethernet cable. Wifi is not reliable enough to detect the ARP requests from the button.
2. Clone this repo

#### Set up the script

1. `pip3 install scapy-python3 googlemaps twilio`
2. `touch keys.py`
3. Add your API keys to keys.py like so:
```python
mac_address = "xx:xx:xx:xx" # add the mac address of your dash button in lower case
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

You'll likely need to run the script as root. You also might need to `apt-get install tcpdump`. On a Raspberry Pi I had to update some existing packages to fix some conflicts.
