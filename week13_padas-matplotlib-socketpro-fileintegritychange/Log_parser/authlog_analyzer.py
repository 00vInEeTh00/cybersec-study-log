import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

authlog = "/var/log/auth.log"

suspicious_keywords = [
    "failed password", "authentication failure", "invalid user",
    "error", "refused", "not valid"
]
privilege_keywords = ['sudo', 'pkexec', 'opened for user root', 'USER=root','polkitd']
priv_frequency = {"sudo", "su", "pkexec", "passwd","systemd-userdbd", "polkitd","login", "sshd", "CRON"}



# ---- FIRST PASS: COLLECT PRIVILEGE EVENTS ----
priv_events = []

with open(authlog) as file:
    for line in file:
        match = re.match(
            r'^(?P<date>[\d\-T\:\.]+(?:\+\d{2}:\d{2}))\s(?P<host>[\w\-]+)\s(?P<process>\w+)(?:\[(?P<pid>\d+)\])?\:?\s(?P<message>.+)$',
            line
        )
        if match:
            row = match.groupdict()
            message = row['message']
            process = row['process']

            if process in priv_frequency:
                user_match = re.search(r'(\w+)\s*:', message)

                if user_match:
                    user = user_match.group(1)
                    priv_events.append((user, message))

# count repeated commands
freq = Counter(priv_events)

# ---- SECOND PASS: WRITE CSV WITH FREQUENCY ----
with open(authlog) as file, open('parsed.csv', 'w') as out:
    out.write("date,host,process,pid,message,suspicious,privilege_escalation,frequency\n")

    for line in file:
        match = re.match(
            r'^(?P<date>[\d\-T\:\.]+(?:\+\d{2}:\d{2}))\s(?P<host>[\w\-]+)\s(?P<process>\w+)(?:\[(?P<pid>\d+)\])?\:?\s(?P<message>.+)$',
            line
        )
        if match:
            row = match.groupdict()
            message = row['message']
            process = row['process']


            # suspicious / privilege detection
            is_suspicious = any(k.lower() in message.lower() for k in suspicious_keywords)
            is_privilege = any(k.lower() in (process + " " + message).lower() for k in privilege_keywords)

            #if process in ["CRON", "pkexec"]:
                #is_suspicious = False

            # detect frequency
            frequency = 0
            if process in priv_frequency:
                user_match = re.search(r'(\w+)\s*:', message)

                if user_match:
                    user = user_match.group(1)
                    frequency = freq[(user, message)]

            # write line
            out.write(
                f"{row['date']},{row['host']},{row['process']},{row['pid']},"
                f"\"{message}\",{is_suspicious},{is_privilege},{frequency}\n"
            )


           

df = pd.read_csv("parsed.csv",parse_dates=['date'])

# Count privilege escalation events by process
priv_esc_count = df[df['privilege_escalation']==True].groupby('process').size()
suspicious_logs = df[df['suspicious']==True]
suspicious_logs.to_csv("suspicious_logs.csv", index=False)

plt.figure(figsize=(8,4))
priv_esc_count.plot(kind='bar')
plt.title('Privilege Escalation Events by Process')
plt.xlabel('Process')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()


suspicious_count = df[df['suspicious']==True].groupby('process').size()

plt.figure(figsize=(8,4))
suspicious_count.plot(kind='bar', color='red')
plt.title('Probability of Suspicious Activity by Process')
plt.xlabel('Process')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()









# make sure all the keywords that looking is case sensitive so never miss anything.
