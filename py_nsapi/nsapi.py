"""
Voor gebruik van de webservice is aparte autorisatie vereist.
Deze autorisatie wordt verleend na ontvangst van een getekend contract.
Dit contract is op te vragen via nsr.api@ns.nl.
"""
import logging
import os
import sys

import requests
import xmltodict

_PRICES = (
    "http://webservices.ns.nl/ns-api-prijzen-v3"
    "?from={from_station}"
    "&to={to_station}"
    "&via={via_station}"
    "&dateTime={date_time}"
)
_DEPARTURE_TIMES = "https://webservices.ns.nl/ns-api-avt?station={station}"
_DISRUPTIONS = (
    "http://webservices.ns.nl/ns-api-storingen?station={station}"
    "&actual={actual}"
    "&unplanned={unplanned}"
)
_TRAVEL_ADVICE = (
    "http://webservices.ns.nl/ns-api-treinplanner"
    "?fromStation={from_station}"
    "&toStation={to_station}"
    "&viaStation={via_station}"
    "&previousAdvices={previous_advices}"
    "&nextAdvices={next_advices}"
    "&dateTime={date_time}"
    "&Departure={departure}"
    "&hslAllowed={hsl_allowed}"
    "&yearCArd={year_card}"
)
_STATIONS = "http://webservices.ns.nl/ns-api-stations-v2"


class Trains:
    def __init__(self, usr=None, pwd=None):
        try:

            # Check if username and password are into place and set them
            if self.is_not_empty(usr) and self.is_not_empty(pwd):
                self.usr = usr
                self.pwd = pwd
            else:
                raise Exception("You must provide a username and password for the API.")

        except Exception as e:
            self._parse_exception(e)

    def go_fetch(self, url):

        try:
            # get the data with authentication from NS API

            r = requests.get(url, auth=(self.usr, self.pwd))

            if r.status_code != 200:
                raise Exception(f"NS Connection failure {r.status_code}")

            return r.text

        except Exception as e:
            self._parse_exception(e)

    def is_not_empty(self, s):
        return s is not None and bool(s.strip())

    @staticmethod
    def _parse_exception(e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logging.warning(f"{e} | {exc_type} | {fname} | {exc_tb.tb_lineno}")


class Prijzen(Trains):
    """Fetch and parse NS train pricing data."""

    def get_data(
        self, from_station=None, to_station=None, via_station="", date_time=""
    ):
        try:
            if from_station is None or to_station is None:
                raise Exception("You must provide a From and To station")

            # fetch the elements from the NS API
            url = _PRICES.format(
                from_station=from_station,
                to_station=to_station,
                via_station=via_station,
                date_time=date_time,
            )

            root = self.go_fetch(url)

            return xmltodict.parse(root, dict_constructor=dict)

        except Exception as e:
            self._parse_exception(e)


class Vertrektijden(Trains):
    """Fetch and parse NS train departure data."""

    def get_data(self, station=None):
        try:
            if self.is_not_empty(station):
                # fetch the elements from the NS API
                url = _DEPARTURE_TIMES.format(station)
                root = self.go_fetch(url)

                # parse elements into dict
                elements = xmltodict.parse(root, dict_constructor=dict)

                if elements["ActueleVertrekTijden"] is not None:
                    return elements["ActueleVertrekTijden"]
                else:
                    return False

            else:
                raise Exception("You should use a station")

        except Exception as e:
            self._parse_exception(e)


class Storingen(Trains):
    """Fetch and parse NS train failures data."""

    def get_data(self, station="", actual=True, unplanned=""):
        try:

            # fetch the elements from the NS API
            url = _DISRUPTIONS.format(
                station=station,
                actual=str(actual).lower(),
                unplanned=str(unplanned).lower(),
            )

            root = self.go_fetch(url)

            # parse elements into dict
            elements = xmltodict.parse(root, dict_constructor=dict)

            if elements["Storingen"] is not None:
                return elements["Storingen"]
            else:
                return False

        except Exception as e:
            self._parse_exception(e)


class Reisadviezen(Trains):
    """Fetch and parse NS train advice data"""

    def get_data(
        self,
        from_station=None,
        to_station=None,
        via_station="",
        previous_advices=2,
        next_advices=3,
        date_time="",
        departure="true",
        hsl_allowed="true",
        year_card="false",
    ):
        """
        Let op: bij unplanned=true worden de geplande werkzaamheden geretourneerd.
        Dit is dus net andersom dan wat de parameternaam doet vermoeden.
        """
        try:
            if from_station is None or to_station is None:
                raise Exception("You have to put in a From Station and To Station")

            url = _TRAVEL_ADVICE.format(
                from_station=from_station,
                to_station=to_station,
                via_station=via_station,
                previous_advices=previous_advices,
                next_advices=next_advices,
                date_time=date_time,
                departure=str(departure).lower(),
                hsl_allowed=str(hsl_allowed).lower(),
                year_card=str(year_card).lower(),
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
            self._parse_exception(e)


class Stations(Trains):
    """Fetch and parse NS train stations data."""

    def get_data(self):
        try:
            # fetch the elements from the NS API
            url = _STATIONS
            root = self.go_fetch(url)

            # parse elements into dict
            elements = xmltodict.parse(root, dict_constructor=dict)

            if elements["Stations"] is not None:
                return elements["Stations"]
            else:
                return False

        except Exception as e:
            self._parse_exception(e)
