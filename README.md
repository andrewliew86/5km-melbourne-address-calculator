# 5km-melbourne-address-calculator
Try out the app here: https://share.streamlit.io/andrewliew86/5km-melbourne-address-calculator/main/distance.py

Background:
During the June 2021 Melbourne lockdown, the Victorian government initiated a 2-week lockdown of Melbourne to curb the outbreak of COVID-19 with residents only being allowed to travel within a 5km bubble. The distance shown on Google maps is often not a 'straight line' between locations so cannot be used to determine if a location is within 5km of your home.

Results:
This app can be used to determine the approximate 'straight line' distance between two addresses. It uses scikitlearn's haversine distance to calculate the distance between two coordinates (latitutude and longitude). Geoencoding of addresses utilizes the 'positionstack' REST API. The app is hosted on Streamlit.
