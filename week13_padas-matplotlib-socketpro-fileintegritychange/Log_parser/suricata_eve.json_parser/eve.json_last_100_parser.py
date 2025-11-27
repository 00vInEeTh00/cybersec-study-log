from collections import deque
import json


location = "/var/log/suricata/eve.json"

with open(location,"r") as logs:
    last_100 = deque(logs,maxlen=100)

for line in last_100:
        try:
            log = json.loads(line)
        except json.JSONDecodeError:
            continue

        timestamp = log.get("timestamp", "-")
        event_type = log.get("event_type", "-")
        src_ip = log.get("src_ip", "-")
        dest_ip = log.get("dest_ip", "-")

        extra = ""

        if event_type == "dns":
            q = log.get("dns", {}).get("rrname", "")
            extra = f"dns:{q}"
        elif event_type == "http":
            uri = log.get("http", {}).get("url", "")
            extra = f"http:{uri}"
        elif event_type == "tls":
            sni = log.get("tls", {}).get("sni", "")
            extra = f"tls:{sni}"
        elif event_type == "flow":
            proto = log.get("proto", "")
            extra = f"flow:{proto}"
        elif "alert" in log:
            extra = log["alert"].get("signature", "")
        else:
            extra = event_type

        print(f"{timestamp},{event_type},{src_ip},{dest_ip},{extra}")





