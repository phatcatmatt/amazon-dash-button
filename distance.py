import googlemaps
from datetime import datetime
from keys import maps_key

def travel_time():
    gmaps = googlemaps.Client(key=maps_key)
    matrix_response = gmaps.distance_matrix('Provo, Utah', 'Salt Lake City, Utah')
    return matrix_response['rows'][0]['elements'][0]['duration']['value']
