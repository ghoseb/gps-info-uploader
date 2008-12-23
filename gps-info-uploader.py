#!/usr/bin/env python
## gps-info-uploader.py -- Upload GPS Info -*- Python -*-
## Time-stamp: "2008-12-23 20:40:23 ghoseb"

## Copyright (c) 2008, Baishampayan Ghose <b.ghose at gmail.com>
"""
Regularly gather information from the mobile phone's GPS receiver and
upload the information to the server.
"""

# import httplib
import positioning

# SERVER_URL = "server.url"
# SERVER_PATH = "/some/path"
# HTTP_METHOD = "POST"

LOG_FILE = "E:\\gps_log.txt"

positioning.select_module(positioning.default_module())
positioning.set_requestors([{"type":"service",
                             "format":"application",
                             "data":"gps_info_getter"}])

positioning.last_position()

def callback_fn(event):
    """Callback to log GPS info
    
    Arguments:
    - `event`: The info from a GPS event
    """
    fp = open(LOG_FILE, "a")
    fp.write(str(event) + "\n")
    fp.close()
    print "Wrote gps info!"
    
print "I think GPS is working, so trying to log the info..."

positioning.position(callback=callback_fn, partial=0, interval=500000)



