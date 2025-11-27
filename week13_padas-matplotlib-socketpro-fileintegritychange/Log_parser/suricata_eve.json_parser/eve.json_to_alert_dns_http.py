import json
import csv

input_file = '/var/log/suricata/eve.json'
alert_out = '/home/eva/Desktop/tools/log_monitoring/suricata_alert.csv'
http_out = '/home/eva/Desktop/tools/log_monitoring/suricata_http.csv'
dns_out = '/home/eva/Desktop/tools/log_monitoring/suricata_dns.csv'

with open(input_file) as file, \
     open(alert_out, 'a', newline='') as out_alert, \
     open(http_out, 'a', newline='') as out_http,\
     open(dns_out, 'a', newline='') as out_dns:

    alert_writer = csv.writer(out_alert)
    http_writer = csv.writer(out_http)
    dns_writer = csv.writer(out_dns)

    for line in file:
        event = json.loads(line)

        # ALERT EVENTS
        if event.get("alert"):
            timestamp = event.get("timestamp", "N/A")
            signature = event["alert"].get("signature", "N/A")
            src_ip = event.get("src_ip", "N/A")
            dest_ip = event.get("dest_ip", "N/A")

            alert_writer.writerow([timestamp, signature, src_ip, dest_ip])

        # HTTP EVENTS
        if event.get("http"):
            timestamp = event.get("timestamp", "N/A")
            http_method = event["http"].get("http_method", "N/A")
            url = event["http"].get("hostname", "N/A")
            src_ip = event.get("src_ip", "N/A")
            dest_ip = event.get("dest_ip", "N/A")

            http_writer.writerow([timestamp, http_method, url, src_ip, dest_ip])

        if event.get("dns"):
            timestamp = event.get("timestamp", "N/A")
            src_ip = event.get("src_ip", "N/A")
            dest_ip = event.get("dest_ip", "N/A")

            dns_data = event["dns"]
            query_type = dns_data.get("type", "N/A")
            rrname = dns_data.get("rrname", "N/A")
            rcode = dns_data.get("rcode", "N/A")

            answers = dns_data.get("answers", [])
            answer_ips = ",".join([a.get("rdata", "") for a in answers]) if answers else "N/A"

            dns_writer.writerow([
                timestamp, src_ip, dest_ip,
                rrname, query_type, rcode, answer_ips
            ])
