import logging
import os
import sys
import time

import requests


class Trains:
    def __init__(self, usr=None, pwd=None):
        try:

            # Check if username and password are into place and set them
            if self.is_not_empty(usr) and self.is_not_empty(pwd):
                self.usr = usr
                self.pwd = pwd
            else:
                raise Exception("You must provide a username and password for the API")

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(f"{e} | {exc_type} | {fname} | {exc_tb.tb_lineno}")

    def go_fetch(self, url):

        try:
            # get the data with authentication from NS API

            r = requests.get(url, auth=(self.usr, self.pwd))

            if r.status_code != 200:
                raise Exception(f"NS Connection failure {r.status_code}")

            return r.text

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(f"{e} | {exc_type} | {fname} | {exc_tb.tb_lineno}")

    def is_not_empty(self, s):
        # small script to check if not empty and not None
        return bool(s and s.strip())
