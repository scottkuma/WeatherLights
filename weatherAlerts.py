#!/usr/bin/env python

import PiGlowAlerts as PGA
import CheckForAlerts as CFA
import time
import calendar
import pprint
from sys import exit

brightness = 0.5

print "Waking up...."

# modes = name of mode, number of seconds to wait between checking for alerts again
# 900 seconds = 15 minutes
# 600 seconds = 10 minutes
# 300 seconds =  5 minutes
# 120 seconds =  2 minutes
#  60 seconds =  1 minute

def parseMode(currentAlerts):
    print "Parsing..."
    if currentAlerts['TOR']:
        return 'TOR'
    elif currentAlerts['TOW'] and currentAlerts['WRN']:
        return 'TOWWRN'
    elif currentAlerts['TOW']:
        return 'TOW'
    elif currentAlerts['WRN']:
        return 'WRN'
    elif currentAlerts['SEW']:
        return 'SEW'
    elif currentAlerts['WIN']:
        return 'WIN'
    elif currentAlerts['WAT']:
        return 'WAT'
    elif currentAlerts['FOG']:
        return 'FOG'
    elif currentAlerts['SPE']:
        return 'SPE'
    elif currentAlerts['ERR']:
        return 'ERROR'
    else: 
        return 'NONE'

def doChecks():
    wait_times = {'NONE': 900,
                  'TOR': 120,
                  'TOW': 600,
                  'TOWWRN': 60,
                  'WRN': 150,
                  'SEW': 600,
                  'WIN': 600,
                  'SPE': 300,
                  'WAT': 600,
                  'FOG': 300,
                  'ERROR': 60}

    current_mode = "NONE"
    last_mode = "NONE"
    mode_last_set = 0
    wait_until = 0

    while True:
        currtime = time.gmtime()
        currepoch = calendar.timegm(currtime)

        if currepoch >= wait_until:
            CFA.check_for_alerts()
            pp.pprint(CFA.currentAlerts)
            last_mode = current_mode
            current_mode = parseMode(CFA.currentAlerts)
            mode_last_set = currepoch
            wait_until = (mode_last_set + wait_times[current_mode])

        else:
            print "Mode: ", current_mode, " - Waiting...", wait_until - currepoch, " seconds until next weather check..."
	    doModes(current_mode)
            

def doModes(mode):
    # print "Mode: ", mode
    if mode == "NONE":
        glow.noaction()
        time.sleep(60)
    if mode == "TOR":
 	glow.tor(5) 
    if mode == "TOW":
        glow.tow(6)
    if mode == "TOWWRN":
		glow.towwrn(5)
    if mode == "WRN":
        glow.wrn(6)
    if mode == "SEW":
        glow.sew(6)
    if mode == "WIN":
        glow.win(6)
    if mode == "SPE":
        glow.spe()
        time.sleep(60)
    if mode == "WAT":
        glow.wat(4)
    if mode == "FOG":
        glow.fog()
        time.sleep(60)
    if mode == "ERROR":
        glow.error()
        time.sleep(30)

    
pp = pprint.PrettyPrinter(indent=4)

glow = PGA.PiGlowAlerts(brightness)

glow.clear()
glow.initialize()
time.sleep(2)

try:
    doChecks()
except (KeyboardInterrupt, SystemExit):
    glow.clear()
    print "Ending due to KeyboardInterrupt"
    exit(1)
