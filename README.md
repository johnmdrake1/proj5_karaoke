# proj5_karaoke
Project 5 CIS 322, a mapping application for points of interest.

Title: Downtown Eugene Music Venue Map

Author(s): John Drake, with parts pulled from previous projects by Michal Young and John Drake, 
and google maps javascript api tutorials and documentation

Repo: https://github.com/johnmdrake1/proj5_karaoke

My github page: https://github.com/johnmdrake1/

Details:

Google Maps Sources: https://developers.google.com/maps/documentation/javascript/geolocation, 
https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse,
other tutorials found at these links were used for education on google maps javascript api functionality.
Geotest.html contains the code sourced from Google.

Description:

An interactive map application that uses google maps javascript api to display a map with markers at Downtown Eugene's
three most popular music venues and the user's current location(based on browser geolocation, if available) in a browser.

The markers at the three music venues may be clicked. This causes an information window to appear with the name and 
street address of the venue. As soon as the page loads, a marker should appear at the client's reported geolocation
automatically, the street address of this location will appear in an information window on the marker, and the
map itself should center on this marker. The marker does not need to be clicked for the info to appear, unlike the 
venue markers.

Implementation:

The four main components of the application are:
templates/geotest.html-The page that is displayed in the client, using javascript and the google maps api. The information that
got sent over via mapserver.py is retrieved via jinja2.

mapserver.py-Flask server implementation that serves to send information to geotest.html, including the venue locations/names/addresses from
venues.txt and my google maps api key from credentials.ini.

data.py-functions that read the data in venues.txt and format it into a list of dictionaries(one dict for each location). This
function is called in mapserver.py to get the data and pass it on.

venues.txt- The relevant data for the mapping application. Contained here are the names, addresses, and lat/long coordinates
for each music venue that has a marker.

Other files include a makefile, credentials.ini(not in repo) with the api key and other details, accompanied by config.py.

Instructions:

For user:

Once server is started, going to http://localhost:8000/ in browser should display a map centered on your current location.
Location will default to a central location in Eugene if geolocation data is not available. Markers lie on music venues in
downtown Eugene. Click any of these to view the name and address of that location.

For developers:
Place credentials.ini in main directory, then:


In terminal/command prompt:

1. cd to proj5_karaoke directory
2. make install (to install virtual environment and necessary dependencies in requirements.txt)
3. make start (to start server)
4. Follow end user instructions above once in client
5. make stop (to stop the server)







