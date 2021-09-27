# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 00:24:22 2021

@author: ashle
"""
## The API that was utilized for this assignment was a Major League Baseball API that showed the current game listings for the day of 9/24/2021, All venues games were being played at, and current games scheduled for the 25th of September.

#Importing the requests and pandas packages 
#Requests installed through conda install requests terminal
import requests
import pandas as pd

#Get request MLB Schedule for 9/24
Jsonresponse = requests.get('http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1')

#Check for 200 status message 
Jsonresponse.status_code
Jsonresponse.json()

#Get request for Venues of all Major and Minor League affliates for 9/24
Jsonresponse2 = requests.get('http://statsapi.mlb.com/api/v1/venues')
#Check for 200 Staus message
Jsonresponse2.status_code
Jsonresponse2.json()

# Get scheduled games for 9/25
Jsonresponse3 = requests.get('http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2021-09-25&endDate=2021-09-25')
Jsonresponse.status_code
Jsonresponse3 = Jsonresponse3.json()

#Create Dataframe for all professional baseball major and minor league venues showing which venues are active for the day and which are not!
Jsonresponse = Jsonresponse2.json()
Jsonresponsevenues = Jsonresponse['venues']
JsonresponsevenuesDf = pd.DataFrame(Jsonresponsevenues)
JsonSimple = pd.DataFrame(Jsonresponse['venues'])







