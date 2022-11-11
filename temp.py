import cira 

cira.auth.KEY_FILE = "../alpc_key.json"

print(cira.Portfolio().positions())