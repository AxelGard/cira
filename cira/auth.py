import json
import alpaca_trade_api as tradeapi
import os

"""
This function let's you interact 
with the Alpaca trade API 
"""

KEY_FILE = ""  # user key file path
APCA_API_KEY_ID = ""
APCA_API_SECRET_KEY = ""


def get_api_keys(): 
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
    
    return APCA_ID, APCA_KEY

def check_keys():
    pass  


def authentication_header():
    """ get's key and returns key in json format """
    global KEY_FILE
    with open(KEY_FILE, "r") as file:
        header = json.load(file)
    return header


def api(version="v2"):
    """ returns object for api """
    APCA_ID, APCA_KEY = get_api_keys()
    # Open the API connection
    api = tradeapi.REST(APCA_ID, APCA_KEY, "https://paper-api.alpaca.markets", version)
    # Get account info
    api.get_account()
    return api
