import json
from typing import Iterable

DEFAULT_PARAM_TRANSLATIONS = {
    "en": {
        "abf_hausnr": "House Number",
        "abf_strasse": "Street",
        "abf_suche": "Search",
        "address_name_number": "Address Name or Number",
        "bezirk": "District",
        "gemeinde": "Municipality",
        "hausnr": "House Number",
        "hausnummer": "House Number",
        "hnr": "House Number",
        "houseNo": "House Number",
        "housenameornumber": "House Name or Number",
        "housenumber": "House Number",
        "housenumberorname": "House Number or Name",
        "hpid": "HPID",
        "kommune": "Municipality",
        "ladeort": "Loading Location",
        "lat": "Latitude",
        "lon": "Longitude",
        "ort": "City",
        "ortsgemeinde": "Local Community",
        "ortsteil": "District",
        "params": "Parameters",
        "postCode": "Postcode",
        "post_code": "Postcode",
        "postcode": "Postcode",
        "stadt": "City",
        "stadtteil": "District",
        "strasse": "Street",
        "teilgebiet": "Subarea",
        "turnus": "Cycle",
        "uprn": "UPRN",
        "zipCode": "ZIP Code",
        "zip_code": "ZIP Code",
        "zipcode": "ZIP Code",
        "zusatz": "Addition",
    },
    "de": {
        "Calendar": "Kalender",
        "addition": "Zusatz",
        "address_postcode": "Postleitzahl",
        "address_street": "Straße",
        "address": "Addresse",
        "adress": "Addresse",
        "area": "Gebiet",
        "bill_number": "Rechnungsnummer",
        "city": "Stadt",
        "city_id": "Stadt ID",
        "client": "Kunde",
        "community": "Gemeinde",
        "company": "Unternehmen",
        "customer": "Kunde",
        "district": "Bezirk",
        "email": "E-Mail",
        "hausnr": "Hausnummer",
        "house": "Haus",
        "houseNo": "Hausnummer",
        "house_name": "Hausname",
        "house_number": "Hausnummer",
        "house_number_or_name": "Hausnummer oder Name",
        "housenumber": "Hausnummer",
        "housenumberorname": "Hausnummer oder Name",
        "lat": "Breitengrad",
        "location": "Position",
        "lon": "Längengrad",
        "method": "Methode",
        "municipal": "Gemeinde",
        "municipality": "Gemeinde",
        "number": "Nummer",
        "password": "Passwort",
        "phone": "Telefon",
        "plz": "PLZ",
        "postCode": "PLZ",
        "post_code": "PLZ",
        "postcode": "PLZ",
        "property_no": "Grundstück Nr.",
        "strasse": "Straße",
        "street": "Straße",
        "streetId": "Straßen ID",
        "street_id": "Straßen ID",
        "street_name": "Straßenname",
        "subdomain": "Subdomain",
        "terretory": "Gebiet",
        "town": "Stadt",
        "types": "Typen",
        "uprn": "UPRN",
        "url": "URL",
        "username": "Benutzername",
        "values": "Werte",
        "version": "Version",
        "village": "Ort",
        "voivodship": "Woiwodschaft",
        "zipCode": "PLZ",
        "zip_code": "PLZ",
        "zipcode": "PLZ",
        "zone": "Zone",
    },
    "it": {
        "addressNo": "Indirizzo Numero",
        "api_key": "Chiave API",
        "bill_number": "Numero della bolletta",
        "building_number": "Numero Edificio",
        "calendar": "Calendario",
        "calendar_splitter": "Calendar Splitter",
        "calendar_title": "Nome Calendario",
        "city": "Città",
        "city_id": "ID Città",
        "city_part": "Parte della Città",
        "client": "Cliente",
        "community": "Comunità",
        "company": "Compagnia",
        "council": "Consiglio",
        "count": "Conteggio",
        "county_id": "ID Paese",
        "customer": "Cliente",
        "dates": "Date",
        "district": "Distretto",
        "district_id": "ID Distretto",
        "door_num": "Numero Interno",
        "email": "Email",
        "excludes": "Escludi",
        "file": "Nome File",
        "frequency": "Frequenza",
        "house": "Casa",
        "houseID": "ID Casa",
        "houseNo": "Civico",
        "house_letter": "Lettera Casa",
        "house_name": "Nome Casa",
        "house_number": "Civico",
        "housenameornumber": "Numero o Nome Casa",
        "housenumber": "Civico",
        "housenumberorname": "Numero o Nome Casa",
        "ignored_containers": "Ignored Containers",
        "interval": "Intervallo",
        "ladeort": "Ladeort",
        "location": "Posizione",
        "location_id": "ID Posizione",
        "method": "Metodo",
        "municipality": "Municipality",
        "municipality_id": "Municipality ID",
        "name": "Nome",
        "number": "Numero",
        "operator": "Operatore",
        "p_collect_cycle": "P Collect Cycle",
        "params": "Parametri",
        "phone": "Telefono",
        "pid": "PID",
        "postCode": "Codice Postale CAP",
        "post_code": "Codice Postale CAP",
        "postal_code": "Codice Postale CAP",
        "postcode": "Codice Postale CAP",
        "predict": "Predict",
        "prem_code": "Premises Code",
        "premises_id": "Premises ID",
        "project_id": "Project ID",
        "property": "Proprietà",
        "propertyID": "ID Proprietà",
        "property_id": "ID Proprietà",
        "property_location": "Posizione Proprietà",
        "property_no": "Proprietà Numero",
        "r_collect_cycle": "R Collect Cycle",
        "radius": "Raggio",
        "region": "Regione",
        "road": "Strada",
        "road_name": "Nome Strada",
        "sector": "Settore",
        "service": "Servizio",
        "service_id": "ID Servizio",
        "service_provider": "Fornitore di Servizi",
        "show_nights": "Mostra Notti",
        "start": "Inizio",
        "state": "Stato",
        "street": "Strada",
        "streetId": "ID Strada",
        "streetIndex": "Indice Strada",
        "streetName": "Nome della Strada",
        "street_address": "Indirizzo Strada",
        "street_code": "Codice Strada",
        "street_id": "ID Strada",
        "street_name": "Nome Strada",
        "street_number": "Numero Strada",
        "street_town": "Città Strada",
        "suffix": "Suffisso",
        "territory": "Territorio",
        "town": "Città",
        "unit_number": "Numero Interno",
        "until": "Fino",
        "uprn": "UPRN",
        "values": "Valori",
        "verify_ssl": "Verifica SSL",
        "version": "Versione",
        "village": "Villaggio",
        "weekdays": "Giorni feriali",
        "zipCode": "Codice Postale CAP",
        "zip_code": "Codice Postale CAP",
        "zipcode": "Codice Postale CAP",
        "zone": "Zona",
        "zoneID": "ID Zona",
        "zone_id": "ID Zona",
    },
    "fr": {
        "abf_hausnr": "Numéro civique",
        "abf_strasse": "Rue",
        "abf_suche": "Recherche",
        "address_name_number": "Numéro et nom de rue",
        "bezirk": "District",
        "gemeinde": "Municipalité",
        "hausnr": "Numéro civique",
        "hausnummer": "Numéro civique",
        "hnr": "Numéro civique",
        "houseNo": "Numéro civique",
        "housenameornumber": "Numéro civique",
        "housenumber": "Numéro civique",
        "housenumberorname": "Numéro civique",
        "hpid": "HPID",
        "kommune": "Municipalité",
        "ladeort": "Chargement de la localisation",
        "lat": "Latitude",
        "lon": "Longitude",
        "ort": "Ville",
        "ortsgemeinde": "Communauté",
        "ortsteil": "District",
        "params": "Paramètres",
        "postCode": "Code Postal",
        "post_code": "Code Postal",
        "postcode": "Code Postal",
        "stadt": "Ville",
        "stadtteil": "District",
        "strasse": "Rue",
        "teilgebiet": "Subarea",
        "turnus": "Cycle",
        "uprn": "UPRN",
        "zipCode": "Code ZIP",
        "zip_code": "Code ZIP",
        "zipcode": "Code ZIP",
        "zusatz": "Addition",
    },
}


DEFAULT_PARAM_DESCRIPTIONS = {
    "en": {
        "uprn": "An easy way to discover your Unique Property Reference Number (UPRN) is by going to https://www.findmyaddress.co.uk/ and entering in your address details.",
    },
    "de": {
        "uprn": "Eine einfache Möglichkeit, Ihre Unique Property Reference Number (UPRN) zu finden, besteht darin, auf https://www.findmyaddress.co.uk/ zu gehen und Ihre Adressdaten einzugeben.",
    },
    "it": {
        "uprn": "Un modo facile per scoprire il tuo Numero di Riferimento Proprietà Unica (UPRN) è andare su https://www.findmyaddress.co.uk/ e inserire i dettagli del tuo indirizzo.",
    },
    "fr": {
        "uprn": "Une manière simple de retrouver votre numéro unique de propriété (UPRN) est de vous rendre sur https://www.findmyaddress.co.uk/ et de saisir les détails de votre adresse."
    },
}


def default_translations(args: Iterable[str]) -> dict[str, dict[str, str]]:
    translation: dict[str, dict[str, str]] = {}
    for arg in args:
        for lang, translations in DEFAULT_PARAM_TRANSLATIONS.items():
            if not lang in translation:
                translation[lang] = {}
            if arg in translations:
                translation[lang][arg] = translations[arg]
    return translation


def default_descriptions(args: Iterable[str]) -> dict[str, dict[str, str]]:
    translation: dict[str, dict[str, str]] = {}
    for arg in args:
        for lang, translations in DEFAULT_PARAM_DESCRIPTIONS.items():
            if not lang in translation:
                translation[lang] = {}
            if arg in translations:
                translation[lang][arg] = translations[arg]
    return translation


def sort_translations():
    for lang in DEFAULT_PARAM_TRANSLATIONS:
        DEFAULT_PARAM_TRANSLATIONS[lang] = dict(
            sorted(DEFAULT_PARAM_TRANSLATIONS[lang].items())
        )
    print(json.dumps(DEFAULT_PARAM_TRANSLATIONS, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    sort_translations()
