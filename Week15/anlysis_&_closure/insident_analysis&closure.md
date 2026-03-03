# SOC Process for Incident Analysis and Closure
**Research Report** **Author:** Vineeth M  
**Date:** 03-03-2026

---

## 1. Incident Analysis – Steps and Process

### 1. Collect Indicators and Precursors
The first step is gathering all available information related to suspicious activity.
* **Sources:** User complaints, Security alerts (IDS/IPS), Firewall logs, System/Application logs, and Monitoring tools.
* **Purpose:** Identify potential signs that an incident might be occurring.

### 2. Validate Indicators (Initial Evaluation)
Analysts must distinguish between a **Security Event** (normal activity) and a **Security Incident** (actual threat to CIA).
* **Check for:** False positives, system failures, misconfigurations, or human error.

### 3. Perform Initial Incident Analysis
Assess the "who, what, where, and how" to prioritize response.
* **Determine:** Affected systems, attack origin (IP/User), tools used, and exploited vulnerabilities.

### 4. Understand Normal System Behavior
Compare current activity against established baselines to identify abnormal deviations.

### 5. Profile Networks and Systems
Establish expected activity baselines, such as:
* File integrity checksums.
* Average network bandwidth usage.
* Standard login patterns.

### 6. Perform Event Correlation
Combine data from multiple sources (e.g., matching a Firewall source IP to an Application username) to validate if an attack succeeded.

### 7. Review and Retain Logs
Maintain log retention policies to reconstruct timelines. Older logs may reveal early reconnaissance activity.

### 8. Synchronize System Time (Timestamp Validation)
All systems must use synchronized clocks (NTP) to ensure accurate timelines and reliable forensic evidence.

### 9. Research Suspicious Activity
Investigate unknown behaviors using internal knowledge bases, threat intelligence (CTI), and internet research for unusual ports or malware indicators.

### 10. Collect Additional Evidence (Packet Capture)
Use packet sniffers to capture raw network traffic if logs lack sufficient detail, following organizational approval procedures.

### 11. Filter and Prioritize Data
Focus resources efficiently by filtering low-risk alerts and prioritizing high-severity indicators.

### 12. Use Knowledge Base and Documentation
Maintain shared references for known indicators and error codes to improve analysis speed and consistency.

### 13. Collaborate and Seek Assistance
Consult internal teams (SysAdmins) or external IR teams/CSIRTs if the analysis is unclear.

### 14. Document Analysis Activities
Record all actions taken, evidence collected, and decisions made for tracking, legal evidence, and future learning.

---

## 2. Steps for Closing Incidents

### 1. Check That All Planned Actions Are Completed
* Review all recorded investigation and containment actions.
* Ensure all actions in the **SIRP** (Security Incident Response Plan) include exact dates and times.
* Check for gaps in understanding or uncorrected attacker activities.

### 2. Confirm Safety of Normal Operations
* Observe affected systems before formal closure.
* Verify the attacker is removed and systems have returned to a stable state.
* Ensure security modifications do not negatively impact interconnected systems.

### 3. Review Legal Obligations
* Fulfill all legal requirements and report to authorities (Police/National Law Enforcement) if required.
* Report personal data breaches to regulatory bodies (e.g., GDPR/HIPAA mandates).

### 4. Communicate With Stakeholders
* Explain the cause and impact of the incident to impacted teams.
* Describe corrective actions taken.
* Provide guidance on avoiding or detecting similar incidents in the future.

### 5. Close the Incident
* Formally close related tickets in the SIRP.
* Update the incident status in the **SOAR** platform.

### 6. Learn From the Incident
* Conduct a post-incident review to evaluate SOC performance.
* Identify specific improvements for future incident handling (e.g., updating playbooks or detection rules).

---

**Summary**
Incident analysis is a rigorous process of validation and correlation, while closure ensures that the organization is not only secure but also compliant and better prepared for the next threat.
