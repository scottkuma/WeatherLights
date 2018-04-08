import requests
import pprint
import calendar
import time
import os
import sys
import cPickle as pickle
from types import *


# ----  USER VARIABLES ----

# The userkey below is to the Weather Underground API
userkey = ""

# Set the location to the ZIP code (if in the US) or other local identifier 
location= "45039"
# ---- END USER VARIABLES ----


# Set the second variable in each list to True if you wish to signal 
# that weather alert type on the PiGlow.

alert_types = {"HUR": ["Hurricane Local Statement", False],
               "TOR": ["Tornado Warning", True],
               "TOW": ["Tornado Watch", True],
               "WRN": ["Severe Thunderstorm Warning", True],
               "SEW": ["Severe Thunderstorm Watch", True],
               "WIN": ["Winter Weather Advisory", True],
               "FLO": ["Flood Warning", False],
               "WAT": ["Flood Watch / Statement", True],
               "WND": ["High Wind Advisory", False],
               "SVR": ["Severe Weather Statement", False],
               "HEA": ["Heat Advisory", False],
               "FOG": ["Dense Fog Advisory", True],
               "SPE": ["Special Weather Statement", True],
               "FIR": ["Fire Weather Advisory", False],
               "VOL": ["Volcanic Activity Statement", False],
               "HWW": ["Hurricane Wind Warning", False],
               "REC": ["Record Set", False],
               "REP": ["Public Reports", False],
               "PUB": ["Public Information Statement", False]}


# Each alert signified with True, above, will need to be set in this list as well.
# Set each to false (except ERR) on startup.

currentAlerts = {"TOR": False,
                 "TOW": False,
                 "WRN": False,
                 "SEW": False,
                 "WIN": False,
                 "SPE": False, 
				 "WAT": False,
                 "ERR": True,
                 "FOG": False,
		 "Phenomena": list()}


def check_for_alerts():
    global currentAlerts
    global userkey
    global location
 
    pp = pprint.PrettyPrinter(indent=4)


    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)

    url = "http://api.wunderground.com/api"
    key = "/" + userkey
    features = "/alerts/conditions"
    settings = ""
    query = "/q/" + location
    responseformat = "json"

    currtime = time.gmtime()
    currepoch = calendar.timegm(currtime)

    fullURL = url + key + features + settings + query + "." + responseformat
    print fullURL
    
    #reset alerts
    for a in currentAlerts:
	print a
	print type(currentAlerts[a])
	if type(currentAlerts[a]) is BooleanType: 
        	currentAlerts[a] = False
	if type(currentAlerts[a]) is ListType:
		currentAlerts[a] = list()

    # pp.pprint( currentAlerts )

    print "Checking for weather alerts..."

    try:
        response = requests.get(fullURL, timeout=(2,10))
    except Exception as e:
        print "Error: ", e
        currentAlerts["ERR"] = True
        alerts = []
    else:
        if response.status_code == 200:
            try:
                jresponse = response.json()
                alerts = jresponse['alerts']
            except Exception as e:
                currentAlerts["ERR"] = True
                alerts = []
                print "Error: ", e 
            print "There are " + str(len(alerts)) + " current weather alerts."

            if len(alerts) > 0:
                for alert in jresponse['alerts']:
                    alert_type = alert['type']
		    print currentAlerts['Phenomena']
		    currentAlerts['Phenomena'].append(alert['phenomena'])
                    alert_text = alert_types[alert['type']][0]
                    alert_action = alert_types[alert['type']][1]
                    print "* " + alert_text
                    expires = alert['expires_epoch']
                    print "  Expires in " + str((int(expires) - currepoch) / 60) + " minutes."

                    if alert_action:
                        currentAlerts[alert_type] = True

    return currentAlerts
