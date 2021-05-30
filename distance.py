import streamlit as st
from math import radians
from sklearn.neighbors import DistanceMetric
import numpy as np
from geopy.geocoders import Nominatim

# Create title of dashboard
st.title("Is it in my 5 Ks?")
st.markdown(
"""
Victorian government has announced new restrictions to curb the spread of COVID-19 in the community. Victorians are only allowed to shop for essential goods and exercise within 5 km of their homes.

You want to support local businesses but when checking on Google maps, your favourite restaurant is 7.3 km from your home. Using an interactive map, you can see that the restaurant is within the 5km radius of your home but you are still a bit unsure. This discrepancy is because the distance shown on Google maps is based on distance travelled rather than the ‘straight line’ distance between two locations (i.e. radius). 

This app allows you to calculate the approximate distance between two locations (origin and destination) using the Haversine distance (angular distance between two points on the surface of a sphere). Now you can be pretty confident that you won’t be fined for trying to support your favourite restaurants.
"""
)


# Input address of origin and destination
origin = st.text_input('Address of origin:', '99 Highett St, Richmond VIC 3121')
destination = st.text_input('Address of destination:', '23 Oliver Ln, Melbourne VIC 3000')
# Instantiate the Nominatim class
geolocator = Nominatim(user_agent="Andrew's app")

# Create a button that runs the code below when I click on it
if(st.button("Go!")):
    try:
        # Create a geolocator object from the origin and destination addresses
        location_origin, location_destination = geolocator.geocode(origin), geolocator.geocode(destination)
        
        # Use the haversine distance metric from scikit learn to calculate distance between the origin and destination
        # See original code here: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
        dist = DistanceMetric.get_metric('haversine')
        
        X = [[radians(location_origin.latitude,), radians(location_origin.longitude)], 
              [radians(location_destination.latitude), radians(location_destination.longitude)]]
        
        # Calculate the pairwise distance. Note that the approximate radius of earth is 6373 km
        distance_sklearn = 6373.0 * dist.pairwise(X)
        final_distance = np.array(distance_sklearn).item(1)
        st.title(f'Distance: {final_distance:.3f} km')
        st.markdown("***")  # Create some space
        
        # Print out the latitude and longitude of the inputs of the address - can be used to check location on Google map
        st.text(f"Latitude and longitude of destination: {location_destination.latitude}, { location_destination.longitude}")
        st.text(f"Latitude and longitude of origin: {location_origin.latitude}, {location_origin.longitude}")
    
    except AttributeError:
        st.title("Could not find distance between locations. Please ensure you have the correct street address(es)!")
    
    
# To run the streamlit app (on local computer), go to command prompt and navigate to the folder containing this .py file using 'cd'
# 'Activate' the anaconda virutal environment containing the streamlit library... type in activate streamlit_app
# Type 'streamlit run distance.py' 
# Obviously change the name of the .py file accordingly
