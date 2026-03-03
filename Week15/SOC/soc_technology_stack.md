# 6. SOC Technology Stack

The modern SOC is built on a layered technology ecosystem. No single tool provides complete coverage; effective security requires integration across multiple platforms.

---

## 6.1 Core Technology Pillars

### SIEM — Security Information and Event Management

The **SIEM** is the cornerstone of SOC operations. It aggregates and normalizes log and event data from across the environment, applies correlation rules and analytics to detect threats, and provides a centralized platform for investigation and case management.

**Leading Platforms:**
- Splunk
- Microsoft Sentinel
- IBM QRadar
- Elastic Security
- Exabeam
- LogRhythm

**Key Capabilities:**
- Real-time event correlation
- Behavioral analytics (UEBA)
- Compliance reporting
- Long-term log storage

**Challenge:**
- Alert fatigue caused by high false positive rates
- Requires continuous tuning and optimization

---

### SOAR — Security Orchestration, Automation, and Response

SOAR platforms automate repetitive SOC workflows such as alert triage, IOC enrichment, ticket creation, and containment actions through predefined playbooks. This dramatically reduces analyst workload and accelerates response times.

**Leading Platforms:**
- Palo Alto XSOAR
- Splunk SOAR
- Microsoft Sentinel Playbooks
- Tines
- Swimlane

**Key Impact:**
- Can reduce manual effort per incident by 80%+ for routine alert types
- Improves consistency and response speed

---

### EDR / XDR — Endpoint & Extended Detection and Response

**EDR** provides deep visibility into endpoint activity including:
- Process creation
- File modifications
- Network connections
- Registry changes

It enables detection and active response such as:
- Endpoint isolation
- Process termination
- Forensic evidence collection

**XDR** extends this telemetry beyond endpoints into:
- Network
- Email
- Cloud
- Identity systems

This creates a unified detection and response platform.

**Leading EDR/XDR Platforms:**
- CrowdStrike Falcon
- Microsoft Defender XDR
- SentinelOne
- Palo Alto Cortex XDR
- Trend Micro Vision One

---

### Threat Intelligence Platforms (TIP)

TIPs aggregate threat intelligence from:
- Commercial feeds
- Open-source intelligence (OSINT)
- ISAC communities
- Internal telemetry

They normalize, deduplicate, and operationalize:
- Indicators of Compromise (IOCs)
- Tactics, Techniques, and Procedures (TTPs)

**Leading Platforms:**
- Recorded Future
- Mandiant Advantage
- ThreatConnect
- OpenCTI (open source)
- MISP (open source)

---

### NDR — Network Detection and Response

NDR solutions monitor east-west and north-south network traffic using:
- Deep packet inspection
- Flow analysis
- Machine learning-based anomaly detection

They identify threats that bypass endpoint security, including:
- Lateral movement
- Command-and-control (C2) communications
- Advanced network-based attacks

**Leading Platforms:**
- Darktrace
- ExtraHop Reveal(x)
- Vectra AI
- Corelight

---

### UEBA — User and Entity Behavior Analytics

UEBA establishes behavioral baselines for users and machines, then alerts on statistically anomalous deviations such as:

- Accessing unusual resources
- Logging in at abnormal hours
- Transferring unusually large volumes of data

UEBA is highly effective for detecting:
- Insider threats
- Compromised credentials
- Privilege abuse

---

### DFIR Tooling — Digital Forensics & Incident Response

DFIR tools support deep investigation and post-incident analysis.

**Memory Analysis:**
- Volatility Framework

**Disk Forensics:**
- Autopsy
- FTK (Forensic Toolkit)

**Network Forensics:**
- Wireshark
- Zeek
- Moloch / Arkime

**Malware Analysis:**
- Any.run
- Cuckoo Sandbox
- VirusTotal
- IDA Pro
- Ghidra

**OSINT Tools:**
- Maltego
- Shodan
- Censys
- SpiderFoot
