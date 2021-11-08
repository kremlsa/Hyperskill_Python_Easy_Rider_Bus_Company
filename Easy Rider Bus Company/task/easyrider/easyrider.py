from collections import defaultdict
import json


data_dict = json.loads(input())
transfer_stops = set()
stops = set()
wrong_stops = []

for j in data_dict:
    if j["stop_name"] in stops:
        transfer_stops.add(j["stop_name"])
    stops.add(j["stop_name"])

for j in data_dict:
    if j["stop_name"] in transfer_stops:
        if j["stop_type"] == "O":
            wrong_stops.append(j["stop_name"])

print("On demand stops test:")
if len(wrong_stops) == 0:
    print("OK")
else:
    print("Wrong stop type: {}".format(sorted(wrong_stops)))

