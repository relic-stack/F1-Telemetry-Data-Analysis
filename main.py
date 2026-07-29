import http.client
http.client.HTTPConnection.debuglevel = 1

import logging
logging.basicConfig(level=logging.DEBUG)

import fastf1
fastf1.set_log_level("DEBUG")

fastf1.Cache.enable_cache("data_cache")

session = fastf1.get_session(2025, "Silverstone", "R")
session.load()