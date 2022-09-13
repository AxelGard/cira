import cira 

cira.auth.KEY_FILE = "../alpc_key.json"

print(cira.Exchange().cryptocurrencies()[0])