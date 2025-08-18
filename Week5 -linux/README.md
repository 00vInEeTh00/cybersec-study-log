
This is my note when learing 5th week



DISK_USAGE=$(df -P "$HOME" | awk 'NR==2 {gsub("%","",$5); print $5}')
CPU_USAGE=$(top -bn2 | grep "Cpu(s)" | tail -n1 | awk '{print $2 + $4}')
MEM_USAGE=$(free -h | grep Mem | awk '{print $3 "/" $2 " (" int($3/$5*100)
 ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6
 


1. What is a Pipe?

    Symbol: |
    It connects two commands.
    It sends the output (result) of the first command
    as input to the second command.
    Think of it like a water pipe:
        The first command is a tap 🚰 (water = data/text)
        The second command is a bucket 🪣 (it collects and uses that data)
echo "Hello World" | wc -w
wc -w → counts the words → 2



2) Redirect > and >> 📄
    > → Write output to a file (overwrite).
    >> → Append output to a file (keep old stuff, add new line at the end).



3) Command substitution $( ... ) 🔄
What it does: Runs a command and stores its output in place.
Example:
TODAY=$(date)
echo "Today is $TODAY"
Output:
Today is Wed Aug 13 15:10:05 IST 2025



wc  Full form: word count
Here’s the mini chart for wc 🪄
Option	What it Counts	Example Output
-l	Lines 📜	wc -l file.txt → tells how many lines are in the file
-w	Words 📝	wc -w file.txt → tells how many words
-c	Characters 🔠	wc -c file.txt → tells how many total characters (including spaces & symbols)



5) $1, $2, … in functions or scripts 🎯
What it does: These are positional parameters.
    $1 = first argument, $2 = second, etc.
Example:
greet(){
  echo "Hello, $1!"
}
greet "Eva"
Output:
Hello, Eva!


6 - awk
Full form: Named after its creators
It’s a text processing tool in Linux.
Reads line by line of text or file.
Breaks each line into fields (columns) automatically.
Lets you search, filter, and format data.
Basic Structure  - awk 'pattern { action }' file

Special Variables in awk

    $1 → first column
    $2 → second column
    $0 → the whole line
    NF → number of fields in the current line
    NR → line number (record number)
    FS → field separator (default is space)


gsub in awk ✂️
What it does: Find & replace inside text.
Example:
echo "19%" | awk '{ gsub("%","",$1); print $1 }'
Output:
19



7) What is grep
    Full form: Global Regular Expression Print (fancy name, I know 😄).
    It searches for matching text in a file or command output.
ex: ls /bin | grep bash  ,  grep -w sh /etc/passwd



Practice 5: Combine more than one pipe

ls -l /bin | grep bash | wc -l
    ls -l /bin → list all files in /bin
    Pipe to grep bash → keep only lines with bash
    Pipe to wc -l → count those lines.



top -bn1
So combined: -bn1
-b → batch mode (good for scripts)
-n1 → only 1 snapshot


ps command
Quick examples
ps → Shows only processes in your current terminal.
ps -e → Shows all processes in the system.
ps aux → Shows all processes with detailed info.
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | less  →   ee the true sorted list for all processes.


 /dev/null
/dev/null → The "black hole" of Linux.
Anything sent here is thrown away forever.
“Hide the output. I don’t care what the path is, I only care if it exists.”









network commands

3️⃣ Common ip options
Option	Meaning	Example
-br	Brief output (short and neat)	ip -br addr
-4	Show only IPv4 addresses	ip -4 addr show
-6	Show only IPv6 addresses	ip -6 addr show
-o	One-line output per interface	ip -o addr show
-c	Colorize output (if supported)	ip -c addr


2️⃣ Common objects in ip command

Here’s the list of the most common ones you’ll use:
Object	What it is	Example command
addr or address	IP addresses on network interfaces	ip addr show
link	Network interfaces (Ethernet, Wi-Fi, etc.)	ip link show
route	Routing table (where packets go)	ip route show
neigh or neighbor	ARP table (maps IP to MAC)	ip neigh show
rule	Policy routing rules	ip rule show
maddr	Multicast addresses	ip maddr show
mroute	Multicast routing table	ip mroute show
netns	Network namespaces (separate network stacks)	ip netns list
tunnel	IP tunnels (encapsulated connections)	ip tunnel show
monitor	Live monitoring of changes	ip monitor all




What is ping?
ping is a network tool used to check if another computer or device is reachable.
It works by sending ICMP Echo Request packets and waiting for ICMP Echo Reply.
It tells you if the device is reachable and how long it takes for data to travel (latency).

Why is ping important?
To check network connection
To test speed/latency between you and a target
To troubleshoot network problems
To see if a website/server is online or offline

Common options for ping
Option	Meaning	Example
-c <count>	Send only a fixed number of pings	ping -c 4 google.com
-i <seconds>	Time between pings	ping -i 2 google.com
-s <size>	Packet size in bytes	ping -s 100 google.com
-4	Use only IPv4	ping -4 google.com
-6	Use only IPv6	ping -6 google.com

How to read ping output
Example:
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=25.3 ms
64 bytes → packet size received
from 8.8.8.8 → reply came from this IP
icmp_seq=1 → sequence number (first packet)
ttl=118 → Time To Live (hops before packet is dropped)
time=25.3 ms → round trip time (latency)
At the end, it also shows:
Packets sent/received
Packet loss
Average time



What is ss?
ss means Socket Statistics.
It’s a Linux command used to check network connections.
Which ports are open
Which programs are using them
Current TCP/UDP connections
It’s faster and more modern than netstat.

Why is ss important?
To see which apps are connected to the internet
To check listening ports (for servers)
To troubleshoot network problems
To check for suspicious connections (security)

4️⃣ Common ss options
Option	Meaning	Example
-t	Show TCP connections only	   ss -t
-u	Show UDP connections only	   ss -u
-l	Show listening (waiting) sockets   ss -l
-n	Show port numbers (not names)	   ss -n
-p	Show process using the socket	   ss -p
-a	Show all connections	           ss -a
-4	Show only IPv4	     ss -4
-6	Show only IPv6	     ss -6

2️⃣ Common filter types
Filter Type	Example	Meaning
Protocol	ss -t	Only TCP connections
State	ss state established	Only connections that are established
Local port	ss sport = :22	Only connections using source port 22
Remote port	ss dport = :443	Only connections going to port 443
Address	ss dst 192.168.1.10	Only connections to this IP
Process name	`ss -p	grep firefox`

What makes a connection “suspicious”?
Connections to strange IP addresses you don’t recognize 🌐
Connections on unusual ports (e.g., not 80/443 for web)
Services listening on all interfaces (0.0.0.0) without reason
Unknown process names or programs you didn’t start




4️⃣ If You Want Stronger Detection

ss = clues only. To confirm malware:

netstat → similar to ss, but older

lsof -i → shows open network files and processes

ps aux → list all processes (check suspicious names)

Virus scan → clamav (Linux antivirus)

Threat IP check → paste IP into VirusTotal or AbuseIPDB







Imagine your PC has:
IP for Wi-Fi → 192.168.1.5
IP for Ethernet → 192.168.0.10
Local loopback → 127.0.0.1
Wildcard IP address




$HOME
It’s a variable.
Already has a value saved → your home folder.

Example:
echo $HOME
Output → /home/eva


$(hostname)
It’s a command substitution.
Runs the command inside and then gives the result.
Example:
echo $(hostname)
Output → eva-PC


























