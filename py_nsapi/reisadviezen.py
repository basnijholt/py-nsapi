#!/usr/bin/python3
import logging
import os
import sys
import time

import requests

import xmltodict

from .trains import Trains


class reisadviezen(Trains):
    """
        class for fetching and parsing NS train advice data
    """

    def get_data(
        self,
        fromStation=None,
        toStation=None,
        viaStation="",
        previousAdvices=2,
        nextAdvices=3,
        dateTime="",
        Departure="true",
        hslAllowed="true",
        yearCArd="false",
    ):
        try:
            """
            Let op: bij unplanned=true worden de geplande werkzaamheden geretourneerd. 
            Dit is dus net andersom dan wat de parameternaam doet vermoeden.
            """
            if fromStation is None or toStation is None:
                raise Exception("You have to put in a From Station and To Station")

            url = "http://webservices.ns.nl/ns-api-treinplanner?fromStation={}&toStation={}&viaStation={}&previousAdvices={}&nextAdvices={}&dateTime={}&Departure={}&hslAllowed={}&yearCArd={}"
            url = url.format(
                fromStation,
                toStation,
                viaStation,
                previousAdvices,
                nextAdvices,
                dateTime,
                str(Departure).lower(),
                str(hslAllowed).lower(),
                str(yearCArd).lower(),
            )

            # fetch the elements from the NS API
            root = self.go_fetch(url)

            # parse elements into dict
            elements = xmltodict.parse(root, dict_constructor=dict)

            if elements["ReisMogelijkheden"] is not None:
                return elements["ReisMogelijkheden"]
            else:
                return False

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(f"{e} | {exc_type} | {fname} | {exc_tb.tb_lineno}")
