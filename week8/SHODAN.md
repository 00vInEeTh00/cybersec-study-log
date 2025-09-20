# Shodan & OSINT Cheat Sheet: Geolocation, Devices, and Services

This is a concise reference of what we've learned about using Shodan to find devices in specific geographical areas.

---

## 1️⃣ Geographical Area Search

* **Filter:** `geo:"latitude,longitude,radius"`
* **Example (Kozhikode, 10 km radius):**

```
geo:"11.2588,75.7804,10"
```

* Radius is in km.
* Limits results to devices near a specific location.

## 2️⃣ Country Filter

* **Filter:** `country:XX` (ISO country code)
* **Example:** Devices in India:

```
country:IN
```

## 3️⃣ Operating Systems

* **Linux devices:**

```
geo:"11.2588,75.7804,10" os:"Linux"
```

* **Windows 7 machines:**

```
geo:"11.2588,75.7804,10" os:"Windows 7"
```

* **Android devices (mostly IoT/emulators):**

```
geo:"11.2588,75.7804,10" os:"Android"
```

> Note: Most phones are behind NAT/firewalls and won’t appear.

## 4️⃣ Ports and Services

* Common port filters:

  * HTTP: `port:80`
  * HTTPS: `port:443`
  * SSH: `port:22`
  * Telnet: `port:23`
  * RDP: `port:3389`
  * ADB (Android Debug Bridge): `port:5555`
* Example: Linux servers with SSH open in Kozhikode:

```
geo:"11.2588,75.7804,10" os:"Linux" port:22
```

## 5️⃣ Routers / IoT / Webcams

* Filter by product or title to find specific devices:

```
geo:"11.2588,75.7804,10" port:80 title:"router"
geo:"11.2588,75.7804,10" port:554 title:"webcam"
geo:"11.2588,75.7804,10" product:"D-Link"
geo:"11.2588,75.7804,10" product:"TP-Link"
```

> Only publicly exposed devices appear. Home devices behind NAT/firewall usually do not.

## 6️⃣ Understanding Shodan Results

* Typical result fields:

  * **IP address** (public IP)
  * **Open ports**
  * **Service/product/banner info**
  * **Operating system**
  * **Location (city, country, coordinates)**
  * **Organization / ISP / ASN**
  * **Web technologies / security info (HSTS, headers, etc.)**
  * **Last seen timestamp**

### Interpreting devices:

* **Server:** Linux or Windows Server, public IP under organization/ISP, running web services.
* **Personal PC:** Usually behind NAT, rarely appears; mostly Windows or macOS.
* **Router / IoT:** Exposes ports like 80, 443, 23, 554; sometimes brand info is visible.

## 7️⃣ Important Notes / Legal Considerations

* Shodan **only shows devices with public IPs**. Private LAN devices are hidden behind NAT/firewalls.
* You **cannot see personal phones or private LANs** directly.
* Accessing or probing devices without permission is **illegal**.
* Use Shodan for **OSINT, research, or legal security testing**.

## 8️⃣ Example Combined Queries

* Linux server with SSH in Kozhikode:

```
geo:"11.2588,75.7804,10" os:"Linux" port:22
```

* Webcam in Kozhikode:

```
geo:"11.2588,75.7804,10" port:554 title:"webcam"
```

* Windows 7 web server in Kozhikode:

```
geo:"11.2588,75.7804,10" os:"Windows 7" port:80
```

* Android IoT device exposed via ADB:

```
geo:"11.2588,75.7804,10" os:"Android" port:5555
```

---

This cheat sheet summarizes all the key concepts we covered about using Shodan for **geographical OSINT searches**.









# Website OSINT Using Shodan - Cheat Sheet

This cheat sheet guides you through gathering OSINT on a website using **Shodan** along with basic DNS and IP tools in Kali Linux.

---

## 1️⃣ Find the Website IP

### Using `dig` or `nslookup`:

```bash
# IPv4 address
dig example.com A
nslookup example.com

# IPv6 address
dig example.com AAAA
```

**Example Output:**

```
example.com.  300  IN  A  172.67.217.83
example.com.  300  IN  A  104.21.16.246
```

> These are the public IPs you can query in Shodan.

---

## 2️⃣ Check MX (Mail) Records

```bash
dig example.com MX
```

**Example Output:**

```
10 mx.zoho.in.
20 mx2.zoho.in.
50 mx3.zoho.in.
```

> Shows email servers and priority; useful for mapping email infrastructure.

---

## 3️⃣ Check TXT Records (SPF/DKIM/DMARC)

```bash
dig example.com TXT
```

> Reveals email policies, domain verification info, and security configurations.

---

## 4️⃣ Shodan Host Lookup

### Basic host info:

```bash
shodan host 172.67.217.83
shodan host 104.21.16.246
```

**Information obtained:**

* Open ports (HTTP, HTTPS, SSH, FTP, RDP, etc.)
* Running services (Apache, Nginx, IIS, databases, IoT)
* Operating system (Linux, Windows, etc.)
* Web technologies / CMS / frameworks
* SSL/TLS certificate info
* Organization / ISP / ASN
* Geo-location (city, country, coordinates)
* Known vulnerabilities (CVEs)

---

### Optional Shodan CLI Filters

* Filter by port:

```bash
shodan host 104.21.16.246 --port 80
shodan host 104.21.16.246 --port 443
```

* Filter by product/service:

```bash
shodan host 104.21.16.246 product:"nginx"
```

* Check for vulnerabilities:

```bash
shodan host 104.21.16.246 --vulns
```

* Find all websites on the same IP:

```bash
shodan search ip:104.21.16.246
```

---

## 5️⃣ Discover Subdomains

* Use **crt.sh** to find SSL certificate info and linked subdomains:

```
crt.sh/?q=%.example.com
```

* Use tools like `Amass` or `Sublist3r` for active subdomain enumeration.

---

## 6️⃣ Reverse DNS Lookup

* Map IPs back to domains:

```bash
dig -x 172.67.217.83
```

> Useful for discovering related domains or virtual hosting.

---

## 7️⃣ Summary Workflow

1. **Domain → IP** (`dig`, `nslookup`)
2. **IP → Shodan** → open ports, services, OS, vulnerabilities, geo-location
3. **Domain → DNS & SSL** → MX, TXT, subdomains
4. **Combine all info** → complete OSINT map of website infrastructure

---

## 8️⃣ Legal & Safety Notes

* Only gather **publicly available information**.
* Do **not** attempt unauthorized access.
* Shodan is for OSINT, research, and security auditing **legally**.

---

This workflow works for **any website** and is fully compatible with **Kali Linux + Shodan CLI**.
