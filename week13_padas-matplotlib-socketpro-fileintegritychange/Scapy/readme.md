
    4 Common ways of host-discovery methods:

 
1. Arp Scan (Address Resolution Protocol)
    What: Send ARP requests on the local subnet and collect ARP replies (gives IP ↔ MAC).
    When: Local LAN only (same broadcast domain). Fast and very reliable.
    Pro: returns MAC addresses; low false-negatives.
    Con: won’t work across routers.

2. ICMP ping scan
    What: Send ICMP Echo Request (ping) and wait for Echo Reply.
    When: Both local and remote networks if hosts allow ICMP.
    Pro: simple and lightweight.
    Con: many hosts/routers drop or rate-limit ICMP → false-negatives.

3. TCP SYN probe (half open scan)
    What: Send TCP SYN to common ports (e.g., 22,80,443); SYN/ACK implies host up.
    When: When ICMP is blocked but TCP ports likely open.
    Pro: finds hosts that block ICMP but accept TCP.
    Con: slightly more intrusive; may trigger IDS/IPS or logs. 

4. UDP probe
     What: Send UDP packets to service ports and infer host from responses (ICMP Port Unreachable or service reply).
     When: When you expect UDP services or need to detect hosts that only speak UDP.
     Pro: can find UDP-only hosts/services.
     Con: slow, unreliable, many false-negatives; often blocked.
