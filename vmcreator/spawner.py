#!/usr/bin/env python2.7

import os
import logging
import requests
import subprocess
import sys
import time
sys.path.insert(0, "/var/www/framework")
import secrets

while True:
    try:
        req_str = 'http://ictf.cs.ucsb.edu/framework/ctf/pending?secret={}'
        games = requests.get(req_str.format(secrets.API_SECRET)).json()
        if 'ctf_hash' in games:
            logging.info("Spawning the creator for", games['ctf_hash'])
            subprocess.Popen("./create_vms.py {}".format(games['ctf_hash']),
                             shell=True)
    except:
        msg = '''Exception while getting the pending CTF or spawning its \
creation'''
        logging.error(msg)
    time.sleep(30)
