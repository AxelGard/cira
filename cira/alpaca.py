import json
import alpaca_trade_api as tradeapi
import os

KEY_FILE = ""  # user key file path
APCA_API_KEY_ID = ""
APCA_API_SECRET_KEY = ""


def authentication_header():
    """ get's key and returns key in json format """
    with open(KEY_FILE, "r") as file:
        header = json.load(file)
    return header


def api():
    """ returns object for api """
    global KEY_FILE
    global APCA_API_KEY_ID
    global APCA_API_SECRET_KEY

    if "APCA_ID" in os.environ:
        APCA_ID = os.environ["APCA_ID"]
        APCA_KEY = os.environ["APCA_KEY"]
    elif KEY_FILE:
        auth_header = authentication_header()
        APCA_ID = str(auth_header["APCA-API-KEY-ID"])
        APCA_KEY = str(auth_header["APCA-API-SECRET-KEY"])
    else:
        APCA_ID = APCA_API_KEY_ID
        APCA_KEY = APCA_API_SECRET_KEY

    # Open the API connection
    api = tradeapi.REST(APCA_ID, APCA_KEY, "https://paper-api.alpaca.markets")
    # Get account info
    api.get_account()
    return api
