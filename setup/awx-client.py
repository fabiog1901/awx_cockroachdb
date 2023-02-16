import requests
from pprint import pprint
AWX_OAUTH2_TOKEN = 'oD9BOesaUQzOv2cfuHKH0MOaCJqM3Z'

# headers = {"User-agent": "python-awx-client", 
#            "Content-Type": "application/json",
#            "Authorization": "Bearer {}".format(AWX_OAUTH2_TOKEN)}

headers = {"User-agent": "python-awx-client",
           "Content-Type": "application/json"
           }

r = requests.get("http://192.168.64.9:30080/api/v2/users", 
                 headers=headers, auth=('fabio', 'fabio'))

pprint(r.json())
