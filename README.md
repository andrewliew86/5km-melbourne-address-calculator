# 5km-melbourne-address-calculator
Try out the app here: https://share.streamlit.io/andrewliew86/5km-melbourne-address-calculator/main/distance.py

This little Streamlit app can be used to determine the approximate distance between two addresses. If the input destination address is within 5km of your origin (home), then you are safe to visit the location during the June 2021 Melbourne lockdown period.

It uses scikitlearn's haversine distance to calculate the distance between two coordinates (latitutude and longitude)
Note that geoencoding of addresses uses geopy nominatim. 
