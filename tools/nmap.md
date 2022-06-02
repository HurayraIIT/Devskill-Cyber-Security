# nmap room on [tryhackme](https://tryhackme.com/room/furthernmap)

## Introduction

nmap is used to perform **port scanning**. This allows us to gather information about **what services** are running on the target server/IP and on **what port**. The more knowledge we can gather about the target the easier our work will become.

On a server, multiple services can run multiple network requests by opening different **ports** on the server.

Every computer has a total of **65535** available ports. But some of these ports are registered as standard (or well-known) ports.

> Well-known ports 0 to 1023 (only accessible by root)
> Registered ports 1024 to 49151
> Dynamic ports or private ports 49152 to 65535

* IANA = Internet Assigned Numbers Authority
* ICANN = Internet Corporation for Assigned Names and Numbers

port 80 - HTTP
port 443 - HTTPS 
port 139 - Windows NETBIOS
port 445 - SMB

**But these can be altered.**

If we want to know which ports are open and running which services, we need to perform a port scan. Nmap can determine if a port is **open, closed, or filtered(usually by a firewall)**. 

Nmap scripting engine can scan for vulnerabilities on the ports we find, and on some cases exploit the vulnerability directly. 

## Nmap switches

- For SYN scan: `-sS`
- For UDP scan: `-sU`
- OS detection: `-O`
- Service version detection: `-sV`
- To increase verbosity: `-v`
- Verbosity level 2: `-vv`
- Save results in 3 format: `-oA`
- Save in normal format: `-oN`
- Save in grepable format: `-oG`
- Aggressive mode (Service detection + OS detection + Traceroute + Common script scanning): `-A`
- Timing template: `-T5` 
- Scan port 80: `-p 80`
- Scan ports 1000-1500: `-p 1000-1500`
- Scan all ports: `-p-`
- Activate scripts from vuln: `--script=vuln`

## Scan Types:

There are 3 basic scan types:
1. TCP connect scan: `-sT`
2. SYN "Half-open" scan: `-sS`
3. UDP scan: `-sU`

Some less common scan types:
4. TCP Null scan: `-sN`
5. TCP FIN scan: `-sF`
6. TCP Xmas scan: `-sX`
7. ICMP ping scan

## TCP Connect Scan

The TCP connect scan uses the 3 way handshake to find status of a port. 

* **When port is open:** At first it sends a **SYN** packet to the target port, if the target port responds with a **SYN/ACK** packet, then the port is open. In that case nmap sends an **ACK** packet and completes the 3 way handshake.

* **When port is closed:** If the target does responds to the **SYN** packet with a **RST** (reset) packet then the port is closed or unused.

* **When a port is filtered by a firewall:** If the target port does not respond at all to the **SYN** packet then the port might be hiding behind a firewall, in which case, the port is marked as **filtered.** 

However, its very easy to configure the firewall to respond with a **RST** packet, which can make it difficult for nmap.

## SYN scan (Half-open/stealth scan):

These scan are similar to TCP connect scan but differs slightly.

* SYN scan returns a **RST** packet after receiving a **SYN/ACK** from the server.
* It can be used to bypass old IDSs(Intrusion Detection System).
* Some applications will not log SYN scans.
* SYN scan is significantly faster than TCP connect scan.

There are some drawbacks here:
* SYN scan requires SUDO privilege because it has to create raw packets.
* Unstable services may break due to SYN scan.

## UDP scan:

UDP scans are stateless. It throws UDP packets and hopes that it makes it. If the server responds with an ICMP ping packet, then the port is **closed**. But if the server does not respond then the port is **open|filtered** and the UDP packet is sent a second time.

UDP scans take a lot of time.

## NULL, FIN and XMAS scan:

These scans are even stealthier than SYN scan. So these scans are used for firewall evasion.

### * NULL SCAN

NULL scans (-sN) are when the TCP request is sent with no flags set at all. As per the RFC, the target host should respond with a **RST** if the port is **closed**.

### * FIN SCAN

FIN scans (-sF) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a **RST** if the port is **closed**.

### * XMAS SCAN

Xmas scans (-sX) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark. 

## ICMP Network Scan:

ICMP Scan (`-sn`) performs a "ping sweep" of the target.

> To ping sweep an IP range:
`nmap -sn 192.168.0.1-254`
`nmap -sn 192.168.0.0/24`
`nmap -sn 172.16.0.0/16` 

## NSE Scripts:

These are written in LUA. NSE scripts can be used to do a variety of things: from scanning for vulnerabilities, to automating exploits for them. The NSE is particularly useful for reconnaisance. 

* safe:- Won't affect the target
intrusive:- Not safe: likely to affect the target
* vuln:- Scan for vulnerabilities
* exploit:- Attempt to exploit a vulnerability
* auth:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
* brute:- Attempt to bruteforce credentials for running services
* discovery:- Attempt to query running services for further information about the network (e.g. query an SNMP server).

[more here](https://nmap.org/book/nse-usage.html)

## Working with the NSE

To use a script:
`nmap -p 80 --script=vuln target.com`
`nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'`

To know about a script:
`nmap --script-help <script-name>`

## Searching for Scripts

Scripts can be found at these two locations:
1. [Nmap website](https://nmap.org/nsedoc/)
2. In the linux machine: `/usr/share/nmap/scripts`

We can find scripts in the file: `/usr/share/nmap/scripts/script.db` by using grep: `grep "ftp" /usr/share/nmap/scripts/script.db`

The same thing can be done with `ls`: `ls -l /usr/share/nmap/scripts/*ftp*`

To search for categories of script: `grep "safe" /usr/share/nmap/scripts/script.db`

To download missing scripts or to add my own scripts to nmap:

Download using `sudo wget -O /usr/share/nmap/scripts/<script-name>.nse https://svn.nmap.org/nmap/scripts/<script-name>.nse`
then do this: `nmap --script-updatedb`

## Firewall Evasion

* `-Pn` to avoid ping scan and treat all ports as alive. It takes a very long time.
* `-f` fragment the packets
* `--mtu <number multiple of 8>` to specify a maximum transmission unit size.
* `--scan-delay <time>ms` to add a delay between packets
* `--badsum` to generate an invalid checksum. Any real TCP/IP stack will not respond, but a firewall will.

## Nmap default help documentation

```
Nmap 7.80 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports consecutively - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```