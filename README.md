# Flask_api
This flask API is an Emailer API which will accept files of particular format(such as HTML,) as input, and then the files would be stored ina bucket in google cloud storage. 

# Steps to run the file in other host system
1. You must install the Client Library for google cloud storage on your local system
2. Create a new service account from the GCP console and download the JSON file containing authentication credentials.
3. Set the environmenal variables to provide the authentication credentials.

You can refer this link to setup the above steps- https://cloud.google.com/storage/docs/reference/libraries
