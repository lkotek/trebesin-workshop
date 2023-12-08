#!/usr/bin/env python3

import requests

req = requests.get("https://getfedora.org")
print(req.status_code)
