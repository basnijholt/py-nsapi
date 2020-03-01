#!/usr/bin/python3
import logging
import os
import sys
import time

import dateutil.parser
import requests

import xmltodict

from .trains import Trains


class storingen(Trains):
    """
        class for fetching and parsing NS train failures data
    """

    def get_data(self, station="", actual=True, unplanned=""):
        try:

            # fetch the elements from the NS API
            url = "http://webservices.ns.nl/ns-api-storingen?station={}&actual={}&unplanned={}".format(
                station, str(actual).lower(), str(unplanned).lower()
            )

            print(url)
            root = self.go_fetch(url)

            # parse elements into dict
            elements = xmltodict.parse(root, dict_constructor=dict)

            if elements["Storingen"] is not None:
                return elements["Storingen"]
            else:
                return False

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(f"{e} | {exc_type} | {fname} | {exc_tb.tb_lineno}")
