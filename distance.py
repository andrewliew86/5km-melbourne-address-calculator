import streamlit as st
from math import radians
from sklearn.neighbors import DistanceMetric
import numpy as np
from geopy.geocoders import Nominatim
import requests 

# Create title of dashboard
st.title("Melbourne lockdown: can I go there?")
st.markdown(
"""
Victorian government has announced new restrictions to curb the spread of COVID-19 in the community. Victorians are only allowed to shop for essential goods and exercise within 5 km of their homes.

You want to support local businesses but when checking on Google maps, your favourite restaurant is 7.3 km from your home. Using an interactive map, you can see that the restaurant is within the 5 km radius of your home but you are still a bit unsure. This discrepancy is because the distance shown on Google maps is based on distance travelled rather than the ‘straight line’ distance between two locations (i.e. radius). 

This app allows you to calculate the approximate distance between two locations (origin and destination) using the Haversine distance (angular distance between two points on the surface of a sphere). Now you can be pretty confident that you won’t be fined for trying to support your favourite restaurants.
"""
)


# Input address of origin and destination
origin = st.text_input('Address of origin:', '99 Highett St, Richmond VIC 3121')
destination = st.text_input('Address of destination:', '23 Oliver Ln, Melbourne VIC 3000')

# Geoencoding needs to be performed to get the latitude and longitude of input addresses
# The default geopy geoencoding service (Nominatim) is not very accurate (can have up to 1-0.5 km error)
# Use Pointstack (https://positionstack.com/documentation) performs more accurate geoencoding (see Excel spreadsheet comparrison)

def geoencoding(address_input):
    """Get latitude and longitude of an input address using position stack. 
    Returns a tuple with lat, lon coordinates of address"""
    url = 'http://api.positionstack.com/v1/forward'
    params = {'access_key': my_secret_access_key,
    'query': address_input,
    'limit': 1}
    resp = requests.get(url=url, params=params)
    data = resp.json()
    lat = data['data'][0]['latitude']
    lon = data['data'][0]['longitude']
    return lat, lon

# Use geoencoding function to obtain the lat and long coordinates of the origin and destination
origin_lat, origin_lon = geoencoding(origin)
dest_lat, dest_lon = geoencoding(destination)
#%%
# Create Streamlit app

# Create a button that runs the code below when I click on it
if(st.button("Go!")):
    try:
        # Use the haversine distance metric from scikit learn to calculate distance between the origin and destination
        # See original code here: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
        dist = DistanceMetric.get_metric('haversine')
        
        X = [[radians(origin_lat), radians(origin_lon)], 
              [radians(dest_lat), radians(dest_lon)]]
        
        # Calculate the pairwise distance. Note that the approximate radius of earth is 6373 km
        distance_sklearn = 6373.0 * dist.pairwise(X)
        final_distance = np.array(distance_sklearn).item(1)
        st.title(f'Distance: {final_distance:.3f} km')
        st.markdown("***")  # Create some space
        
        # Print out the latitude and longitude of the inputs of the address - can be used to check location on Google map
        st.text(f"Latitude and longitude of origin: {origin_lat}, {origin_lon}")
        st.text(f"Latitude and longitude of destination: {dest_lat}, {dest_lon}")

    except AttributeError:
        st.title("Could not find distance between locations. Please ensure you have the correct street address(es)!")
    
    
# To run the streamlit app (on local computer), go to command prompt and navigate to the folder containing this .py file using 'cd'
# 'Activate' the anaconda virutal environment containing the streamlit library... type in activate streamlit_app
# Type 'streamlit run distance.py' 

