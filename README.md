# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* This python3 module is for getting the NS Train times

### How do I get set up? ###

* Go To https://www.ns.nl/ews-aanvraagformulier/?0
* Subscribe for the NS API (It's free for 50.000 calls a day)
* Install this script with:
    * pip3 py_nsapi --upgrade (or pip py_nsapi --upgrade )
* ready to use it!

###API's###

####Storingen####
De webservice voor de storingen en werkzaamheden maakt het mogelijk informatie op te vragen over storingen en/of werkzaamheden.

#####Fields#####

id
Traject
Reden
Periode
Bericht
Advies

#####Voorbeeld code#####

####Reisadviezen####
De webservice voor de reisadviezen maakt het mogelijk de NS Reisplanner aan te roepen voor een treinreis van een station naar een station. Een reisadvies bestaat uit meerdere reismogelijkheden, zodat de treinreiziger hier een keuze uit kan maken. Een reismogelijkheid bevat zowel geplande als actuele informatie.

#####Fields#####
AantalOverstappen
ActueleVertrekTijd
GeplandeAankomstTijd
ActueleReisTijd
GeplandeVertrekTijd
GeplandeReisTijd
Status
ActueleAankomstTijd
Optimaal
ReisDeel
- @reisSoort
- Status
- Vervoerder
- VervoerType
- RitNummer
- ReisStop
-- Naam
-- Tijd
-- Spoor
--- #text
--- @wijziging

#####Voorbeeld code#####


####Stationslijst####
De webservice voor de stationslijst maakt het mogelijk om alle stationsnamen op te vragen. 

#####Fields#####

Code
UICCode
Synoniemen
Type
Land
Lon
Lat
Namen
- Lang
- Middel
- Kort

#####Voorbeeld code#####

####Vertrektijden####
De webservice voor de actuele vertrektijden maakt het mogelijk om voor een station een actueel overzicht op te vragen van alle vertrekkende treinen voor het komende uur.

#####Fields#####

RitNummer
EindBestemming
Vervoerder
VertrekSpoor
- #text
- @wijziging
RouteTekst
VertrekTijd
TreinSoort

#####Voorbeeld code#####

####Prijzen API#####
De webservice voor de prijzen maakt het mogelijk voor een treinreis de bijbehorende prijsinformatie op te vragen.

Voor gebruik van de webservice is aparte autorisatie vereist. 
Deze autorisatie wordt verleend na ontvangst van een getekend contract. 
Dit contract is op te vragen via nsr.api@ns.nl.

#####Fields#####

#####Voorbeeld code#####




### Who do I talk to? ###

* Theodorus van der Sluijs
* theo@vandersluijs.nl

### License ###
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

####You are free to:####

* Share — copy and redistribute the material in any medium or format
* Adapt — remix, transform, and build upon the material

-The licensor cannot revoke these freedoms as long as you follow the license terms.-

####Under the following terms:####

* Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial — You may not use the material for commercial purposes.
* ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

###NS Disclaimer###
De getoonde prijsinformatie is niet afkomstig van NS reizigers B.V. of een hieraan gelieerde partij. Jegens NS Reizigers B.V. of daaraan gelieerde partijen, kunnne dan ook geen rechten worden ontleend met betrekking tot deze prijsinformatie


###Special thanks to####
Stefan de Konink who gave me a complete new insight with his python api
https://github.com/NS-API/Python-API