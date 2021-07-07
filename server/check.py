# google sheet package
from gsheets import Sheets

# Authorizing the api
sheets = Sheets.from_files('clients.json', 'clients_cache.json')

# Fetching information from signup database
vi1 = sheets.get('1jmi1eB1G7ZQF_SdDtkPBsVz75CrYKarYvdOgYE7L-Bc')

vi1_form1_ws = vi1.sheets[0]

entries1 = vi1_form1_ws.values()[1:]

entries1 = [(i[1], i[2]) for i in entries1]

print(entries1)
