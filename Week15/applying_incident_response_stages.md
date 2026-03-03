# Applying the Six Incident Response Stages in SOC Operations
**Research Report** **Author:** Vineeth M  
**Date:** 03-03-2026

---

## Incident A: Ransomware Execution on Endpoint

**Scenario:** User reports that files are not opening and have a `.encrypted` extension. A pop-up demands Bitcoin payment. The EDR alert shows `powershell.exe` encoding and executing a base64 script.

### 1. Preparation
* **Tools:** EDR (CrowdStrike/SentinelOne), Next-Gen AV, Network segmentation, Offline backups (tested).
* **Playbooks:** Predefined Ransomware Runbook.

### 2. Identification (Detection & Analysis)
* **SOC Actions:**
    * Verify the alert in the EDR console (Process Tree: `explorer.exe` -> `powershell.exe` -> `schtasks.exe`).
    * Check file reputation hashes against VirusTotal.
    * **Correlate with network logs:** Is the workstation communicating with known C2 domains (Tor exit nodes, ransomware leak sites)?
    * **Determine Scope:** Does the user have mapped network drives? Are other assets communicating with the same IP?
* **Documentation:** "Identified malicious process on host WS-102. User 'jdoe' reported file encryption at 09:05. IoCs: Hash 0x... Domain malicious.tld."

### 3. Containment (Short & Long Term)
* **Short-Term (Stop the bleeding):**
    * **Isolate the Host:** Immediately use EDR feature to "Network Isolate" the workstation. Prevents lateral movement and encryption of network shares.
    * **Block IoCs:** Add C2 domain and IP to the firewall/Proxy blocklist.
* **Long-Term:**
    * If the ransomware tried to spread via SMB (port 445), temporarily block outbound SMB at the firewall for the affected subnet.
    * Disable compromised user account (`jdoe`) to prevent credential abuse.

### 4. Eradication
* **Endpoint:** Use EDR to "Kill Process" and "Quarantine" the malicious files.
* **Persistence:** Check for scheduled tasks or registry run keys created by the malware; remove them or factory reset.
* **Credential Reset:** Force password reset for the affected user after confirming the machine is clean.

### 5. Recovery
* **Restoration:** Restore affected local files from backup (OneDrive/Shadow Copies if not encrypted, else offline backup).
* **Un-isolate:** Carefully reconnect the workstation to the network.
* **Validation:** Run another full AV scan to ensure no remnants exist.

### 6. Lessons Learned
* **Root Cause:** How did it get in? (e.g., Malicious macro in email, drive-by download).
* **Gap Analysis:** Did the user have unnecessary admin rights? (Principle of Least Privilege).
* **Documentation:** Update the playbook to block specific PS1 file extensions at the email gateway.

---

## Incident B: DDoS Attack (Web Server)

**Scenario:** Website latency spikes to 10 seconds. Network team reports incoming traffic from thousands of unique IPs targeting the `search.php` endpoint.

### 1. Preparation
* **Tools:** DDoS mitigation service (Cloudflare, AWS Shield), rate-limiting configured on WAF, Auto-scaling groups.

### 2. Identification
* **SOC Actions:**
    * Correlate Web Server logs with Network Flow logs.
    * **Identify Vector:** Is it Layer 7 (HTTP flood) or Layer 3/4 (SYN flood)?
    * **Check Patterns:** Are they hitting one URL? Same User-Agent? Specific query strings?
* **Documentation:** "Layer 7 HTTP flood detected against web01. Traffic volume increased by 5000%. Attack pattern: 'GET /search.php?q=random'."

### 3. Containment
* **Immediate (Redirect/Scrub):**
    * **Enable "Under Attack Mode":** If using Cloudflare, enable "I'm Under Attack" mode (presents a JS challenge).
    * **Rate Limiting:** Implement Geo-blocking or IP reputation filtering at the WAF.
    * **Blackhole:** If internal and under severe L3 attack, trigger BGP Blackhole routing (last resort).

### 4. Eradication
* *Note: You cannot "eradicate" the attacker's botnet. Eradication here means removing the malicious traffic flow.*
* **Actions:** Fine-tune WAF rules to block the specific attack pattern.
* **Analysis:** Pull a PCAP (Packet Capture) of the attack for potential legal action or post-mortem.

### 5. Recovery
* **Traffic Normalization:** Once traffic subsides, disable aggressive mitigation modes.
* **Service Validation:** Ensure legitimate users can access the site and transactions are processing normally.

### 6. Lessons Learned
* **Scalability:** Did the auto-scaling work, or did we have to manually intervene?
* **Monitoring:** Tune thresholds to alert sooner on traffic volume spikes.
