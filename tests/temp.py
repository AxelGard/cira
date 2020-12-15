import cira
import os


if 'APCA_ID' in os.environ and 'APCA_KEY' in os.environ: # github action
    cira.APCA_API_KEY_ID = os.environ['APCA_ID']
    cira.APCA_API_SECRET_KEY = os.environ['APCA_KEY']
    cira.KEY_FILE = ""
else:
    cira.KEY_FILE = "../paper-trader/key.json"


print(cira.list_orders())