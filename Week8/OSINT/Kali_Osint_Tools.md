more: https://afsh4ck.gitbook.io/ethical-hacking-cheatsheet/recopilacion-de-informacion/google-hacking/google-dorks
# Kali Linux OSINT Tools Overview

This is a simple overview of Kali Linux OSINT tools and their uses. Each tool has a short description to help beginners understand its purpose.

---

## 1. Social Media & People Search

* **theHarvester**: Collects emails, subdomains, names, and IPs from public sources.
* **Sherlock**: Searches usernames across 1000+ social networks.
* **twint**: Scrapes Twitter data without using the Twitter API (may need manual install).

---

## 2. Domain / Network Info

* **dnsenum**: Enumerates DNS records for a domain.
* **dnsrecon**: Performs DNS reconnaissance and gathers subdomain info.
* **sublist3r**: Finds subdomains of a target domain.
* **recon-ng**: A full OSINT framework for domain, email, and IP reconnaissance.
* **whois**: Gets domain registration information.

---

## 3. Email / Phone / Leaks

* **theHarvester**: Can also find emails and domains.
* **Email Hunter / Email Permutator**: Generates possible email addresses (manual install).
* **Have I Been Pwned scripts**: Checks if an email address has been part of a data breach.

---

## 4. Metadata / Files

* **exiftool**: Extracts metadata from images, documents, and media files.
* **pdf-parser / pdfid**: Analyzes PDF files for hidden or suspicious data.
* **binwalk**: Inspects binary files to find embedded data.

---

## 5. Visualization / Graph Tools

* **Maltego CE**: Visualizes relationships between people, emails, domains, and social networks (needs installation).
* **Gephi**: Creates interactive network graphs from CSV or other data.
* **recon-ng**: Includes some graph visualization modules for OSINT data.

---

## 6. Frameworks / Automation Tools

* **SpiderFoot**: Automated OSINT tool for scanning domains, IPs, emails, and more (needs manual installation).
* **theHarvester**: Quick OSINT gathering.
* **recon-ng**: OSINT framework with modular approach.

---

**Tips:**

* Start with **theHarvester + recon-ng** for general OSINT tasks.
* Export results to CSV for visualization in **Maltego** or **Gephi**.
* Always use **public data only** to stay ethical.

---

*This overview is beginner-friendly and helps you pick the right tool for the right OSINT task.*
