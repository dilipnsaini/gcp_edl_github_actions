import requests

URL = "https://www.gstatic.com/ipranges/cloud.json"
OUTPUT = "gcp_edl.txt"

data = requests.get(URL, timeout=10).json()

with open(OUTPUT, "w") as f:
   for entry in data["prefixes"]:
       if "ipv4Prefix" in entry:
           f.write(entry["ipv4Prefix"] + "\n")
