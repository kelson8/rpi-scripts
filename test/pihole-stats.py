import psutil
import requests
import json

from dotenv import load_dotenv
import os
# https://blog.gitguardian.com/how-to-handle-secrets-in-python/

# Load the .env file, move api keys in there, so I don't accidently commit them.
load_dotenv()

# Move api key and website into .env
web_password = os.getenv("PIHOLE1_API_KEY")
website = os.getenv("PIHOLE1_WEBSITE")
#

# This might be useful: https://github.com/sdebby/APiHole/blob/main/APiHole/APiHole.py

pihole_api = "/api.php"
pihole_website = website + pihole_api + "/"
kcnet_msg = "KCNet:"
error_msg = "Error:"
auth = "&auth=" + web_password

# I used this to help out:
# https://chrisbergeron.com/2018/06/21/pihole_api/

# I was missing /api.php, traefik automatically adds the /admin part to the url.

# https://discourse.pi-hole.net/t/how-to-auth-when-accessing-the-pihole-api-from-python/4254/2
# def get_pihole(url, query, auth_=""):
#     if auth_ == "":
#         resp = requests.get(url + query)
#     else:
#         resp = requests.get(url + query + auth_)
#     json_data = resp.json()
#     # json_data = json.loads(phpData.json())
#     print(query + "=")
#     print(str(json_data) + "\n")
#     return

# https://github.com/Maschine2501/PiHole-UI/blob/master/dual-z.py
def get_pihole(query):
    # req = requests.get(pihole_website + "/admin/api.php")
    req = requests.get(pihole_website + query + auth)
    data = req.json()



    if req.status_code == 404:
        print(f"{error_msg} File not found!")
    elif req.status_code == 403:
        print(f"{error_msg} Access forbidden to resource.")


    # print(data["status"])

    if query == "?summaryRaw":
        # Why do these give an error?
        # ads_blocked_today = data["ads_blocked today"]
        # ads_percentage_today = data["ads_percentage_today"]

        # print("Blocked: " + str(data["ads_blocked_today"]) + str(data["ads_percentage_today"]))
        # This works
        # print("Blocked: %d (%d%%)" % (data["ads_blocked_today"], data["ads_percentage_today"]))
        print(data)

# get_pihole("?status")
get_pihole("?summaryRaw")
# get_pihole(pihole_website, "?topItems", auth)