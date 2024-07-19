from os import environ

from dotenv import load_dotenv

from utils import str_to_bool

load_dotenv(".env", override=True)

TIMEFORMAT = "%Y-%m-%dT%H:%MZ"
PARKKI_HOST = environ.get("PARKKI_HOST", None)
PARKKI_HTTP_HOST = environ.get("PARKKI_HTTP_HOST", None)
PARKKIOPAS_HOST = environ.get("PARKKIOPAS_HOST", None)
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"ApiKey {environ.get('TOKEN_KEY', None)}",
}
TEST_DOMAIN = environ.get("TEST_DOMAIN", None)
TEST_PAYMENT_ZONE_NUMBER = environ.get("TEST_PAYMENT_ZONE_NUMBER", None)
TEST_EXTERNAL_ID = environ.get("TEST_EXTERNAL_ID", None)
TEST_PERMIT_SERIES_ID = environ.get("TEST_PERMIT_SERIES_ID", None)
TEST_PERMIT_AREA_IDENTIFIER_1 = environ.get("TEST_PERMIT_AREA_IDENTIFIER_1", None)
TEST_PERMIT_AREA_IDENTIFIER_2 = environ.get("TEST_PERMIT_AREA_IDENTIFIER_2", None)
TEST_EVENT_PARKING = str_to_bool(environ.get("TEST_EVENT_PARKING", False))
TEST_EVENT_AREA_ID = environ.get("TEST_EVENT_AREA_ID", None)
TEST_EVENT_AREA_LONGITUDE = float(environ.get("TEST_EVENT_AREA_LONGITUDE", 0.0))
TEST_EVENT_AREA_LATITUDE = float(environ.get("TEST_EVENT_AREA_LATITUDE", 0.0))
TEST_HTTP = str_to_bool(environ.get("TEST_HTTP", False))
