# Module 4: Protecting the Organization

Welcome to this module, which will outline the various strategies and tools used by cybersecurity professionals to protect an organization’s network, data and equipment from cybercrime.

You only have to look at the news to understand that all organizations, regardless of type, size or location, are at risk of a cyber attack. It seems that no one is safe.

So is there anything you can do to help protect an organization from a targeted attack? And with many in the security industry predicting that it’s not a case of ‘if’ but ‘when’ a cybersecurity breach will occur, how can you respond to ensure that it has minimal impact?

This module will highlight the actions that you can take to help answer these questions.

Scroll down  and select 'Cybersecurity Devices and Technologies' to begin.

## 1. Cybersecurity Devices and Technologies

There is no single security appliance or piece of technology that will solve all the network security needs in an organization. You must consider what tools will be most effective as part of your security system.

###  4.1.1 Security Appliances

Security appliances can be standalone devices like a router or software tools that are run on a network device. They fall into six general categories.

>  Routers

While routers are primarily used to interconnect various network segments together, they usually also provide basic traffic filtering capabilities. This information can help you define which computers from a given network segment can communicate with which network segments.

>  Firewalls

Firewalls can look deeper into the network traffic itself and identify malicious behavior that has to be blocked. Firewalls can have sophisticated security policies applied to the traffic that is passing through them.

>  Intrusion prevention systems

IPS systems use a set of traffic signatures that match and block malicious traffic and attacks.

>  Virtual private networks

VPN systems let remote employees use a secure encrypted tunnel from their mobile computer and securely connect back to the organization’s network. VPN systems can also securely interconnect branch offices with the central office network.

>  Antimalware or antivirus

These systems use signatures or behavioral analysis of applications to identify and block malicious code from being executed.

>  Other security devices

Other security devices include web and email security appliances, decryption devices, client access control servers and security management systems.

###  4.1.2 Which Is It?

That’s interesting! You wonder what security system is being implemented at @Apollo.

You ask the Chief Technology Officer (CTO), who explains that the following security appliances are in place. Can you identify which category each of these falls into? You have a chance to earn some defender points, so choose your answers carefully.

Select an option from each of the dropdowns, then Submit.



Well done, that was tricky!

But you managed to correctly identify the security appliances in place and have ensured the safety of @Apollo from cyber attack… for now!

In summary, the security appliances in place are:

* Cisco Integrated Services Router (ISR) 4000. These routers have many capabilities, including traffic filtering, the ability to run an intrusion prevention system (IPS), encryption and VPN capabilities for secure encrypted tunneling.

* Cisco’s Firepower 4100 Series is a next generation firewall that has all the capabilities of an ISR router, as well as advanced network management and analytics. It can help you to see what’s happening on the network so that you can detect attacks earlier.

* Cisco’s AnyConnect Secure Mobility Client is a VPN system that lets remote workers use a secure encrypted tunnel from their mobile computer to securely connect back to the organization’s network. All Cisco security appliances are equipped with a VPN server and client technology, designed for secure encrypted tunneling.

* Cisco’s Advanced Malware Protection (AMP) is installed in next generation Cisco routers, firewalls, IPS devices and web and email security appliances. It can also be installed as software in host computers.

###  4.1.3 Firewalls

In computer networking, a firewall is designed to control or filter which communications are allowed in and which are allowed out of a device or network. A firewall can be installed on a single computer with the purpose of protecting that one computer (host-based firewall) or it can be a standalone network device that protects an entire network of computers and all of the host devices on that network (network-based firewall).

As computer and network attacks have become more sophisticated, new types of firewalls have been developed, which serve different purposes.

> Network Layer Firewall

This filters communications based on source and destination IP addresses.

> Transport layer Firewall

Filters communications based on source and destination data ports, as well as connection states.

> Application Layer Firewall

Filters communications based on an application, program or service.

> Context Aware Layer Firewall

Filters communications based on the user, device, role, application type and threat profile.

> Proxy Server

Filters web content requests like URLs, domain names and media types.

> Reverse Proxy Server

Placed in front of web servers, reverse proxy servers protect, hide, offload and distribute access to web servers.

> Network Address translation (NAT) Firewall

This firewall hides or masquerades the private addresses of network hosts.

> Host-Based Firewall

Filters ports and system service calls on a single computer operating system.

###  4.1.4 Which One?

The CTO forgot to mention that @Apollo has a few firewalls in place. Based on the following statements, can you identify what category of firewall these are? Answer correctly to earn valuable defender points that will help safeguard @Apollo from attack

That’s right!

You have correctly identified the firewall types and have earned some defender points! Check your progress by clicking on the shield icon in the top right-hand corner of your screen.

Remember:

* A NAT firewall filters communications based on source and destination IP addresses.
* A proxy server filters web content requests like URLs, domain names and media types.
* A host-based firewall filters ports and system service calls on a single computer operating system.

###  4.1.5 Port Scanning

In networking, each application running on a device is assigned an identifier called a port number. This port number is used on both ends of the transmission so that the right data is passed to the correct application. Port scanning is a process of probing a computer, server or other network host for open ports. It can be used maliciously as a reconnaissance tool to identify the operating system and services running on a computer or host, or it can be used harmlessly by a network administrator to verify network security policies on the network.

Select the arrows to find out how to carry out a port scan on a computer on your local home network.

Download and launch a port scanning tool like Zenmap. Enter the IP address of your computer, choose a default scanning profile and press ‘scan.’

The scan will report any services that are running, such as web or email services, and their port numbers.

The scan will also report one of the following responses:

* ‘Open’ or ‘Accepted’ means that the port or service running on the computer can be accessed by other network devices.
* ‘Closed,’ ‘Denied’ or ‘Not Listening’ means that the port or service is not running on the computer and therefore cannot be exploited.
* ‘Filtered,’ ‘Dropped’ or ‘Blocked’ means that access to the port or service is blocked by a firewall and therefore it cannot be exploited.

To execute a port scan from outside of your network, you will need to run it against your firewall or router’s public IP address.

Enter the query ‘what is my IP address?’ into a search engine such as Google to find out this information.

Go to the Nmap Online Port Scanner, enter your public IP address in the input box and press ‘Quick Nmap Scan.’ If the response is open for ports 21, 22, 25, 80, 443 or 3389 then most likely, port forwarding has been enabled on your router or firewall and you are running servers on your private network.

###  4.1.6 What Does It Mean?

Your line manager asks you to evaluate @Apollo’s computer network’s firewall and port security. You execute a port scan, which returns an ‘open’ state response.

Complete the sentence below by filling in the blanks from each of the dropdowns to understand what this means.

That's right.

An ‘open’ state response means that the service running on the network can be accessed by other networks and if the service does contain a vulnerability, it could be exploited by an attacker who could potentially gain access to computers on the network.

It’s important to note that port scanning should be seen as a precursor to a network attack and therefore should never be carried out on public servers on the internet or on an organization's network without permission.

###  4.1.7 Intrusion Detection and Prevention Systems

Intrusion detection systems (IDSs) and intrusion prevention systems (IPSs) are security measures deployed on a network to detect and prevent malicious activities.

> IDS

An IDS can either be a dedicated network device or one of several tools in a server, firewall or even a host computer operating system, such as Windows or Linux, that scans data against a database of rules or attack signatures, looking for malicious traffic.

If a match is detected, the IDS will log the detection and create an alert for a network administrator. It will not take action and therefore it will not prevent attacks from happening. The job of the IDS is to detect, log and report.

The scanning performed by the IDS slows down the network (known as latency). To prevent network delay, an IDS is usually placed offline, separate from regular network traffic. Data is copied or mirrored by a switch and then forwarded to the IDS for offline detection.

> IPS

An IPS can block or deny traffic based on a positive rule or signature match. One of the most well-known IPS/IDS systems is Snort. The commercial version of Snort is Cisco’s Sourcefire. Sourcefire can perform real-time traffic and port analysis, logging, content searching and matching, as well as detect probes, attacks and execute port scans. It also integrates with other third-party tools for reporting, performance and log analysis.

Software is not perfect. And more than ever before, hackers are exploiting flaws in software before creators get a chance to fix them. When they do this, hackers are said to have carried out a zero-day attack!

The ability to detect these attacks in real time, and stop them immediately, or within minutes of occurring, is the ultimate goal.

###  4.1.8 Real-Time Detection

Many organizations today are unable to detect attacks until days or even months after they occur.

Detecting attacks in real time requires actively scanning for attacks using firewall and IDS/IPS network devices. Next generation client and server malware detection with connections to online global threat centers must also be used. Today, active scanning devices and software must detect network anomalies using context-based analysis and behavior detection.

DDoS is one of the biggest attack threats requiring real-time detection and response. For many organizations, regularly occurring DDoS attacks cripple Internet servers and network availability. These attacks are extremely difficult to defend against because the attacks originate from hundreds, even thousands, of zombie hosts, and the attacks appear as legitimate traffic.

###  4.1.9 Protecting Against Malware

One way of defending against zero-day attacks and advanced persistent threats (APTs) is to use an enterprise-level advanced malware detection solution, like Cisco’s Advanced Malware Protection (AMP) Threat Grid.

This is client/server software that can be deployed on host endpoints, as a standalone server or on other network security devices. It analyzes millions of files and correlates them against hundreds of millions of other analyzed malware artifacts for behaviors that reveal an APT. This approach provides a global view of malware attacks, campaigns and their distribution.

###  4.1.10 Security Best Practices

Many national and professional organizations have published lists of security best practices. Some of the most helpful guidelines are found in organizational repositories such as the National Institute of Standards and Technology (NIST) Computer Security Resource Center.

 Next Up...

There are other ways of detecting cyber threats other than looking for malicious signatures.

One way that's becoming more common is behavior-based security, which focuses on detecting suspicious network or user behavior.

Select Next to continue.

## 2. Behavior Approach to Cybersecurity

Great work so far! You are starting to understand the makeup of the security system in place at eLearning company @Apollo.

Let’s keep going...

###  4.2.1 Behavior-Based Security

Behavior-based security is a form of threat detection that involves capturing and analyzing the flow of communication between a user on the local network and a local or remote destination. Any changes in normal patterns of behavior are regarded as anomalies, and may indicate an attack.

>  Honeypots

A honeypot is a behavior-based detection tool that lures the attacker in by appealing to their predicted pattern of malicious behavior. Once the attacker is inside the honeypot, the network administrator can capture, log and analyze their behavior so that they can build a better defense.

>  Cisco’s Cyber Threat Defense Solution Architecture

This security architecture uses behavior-based detection and indicators to provide greater visibility, context and control. The aim is to know who is carrying out the attack, what type of attack they are performing and where, when and how the attack is taking place. This security architecture uses many security technologies to achieve this goal.

###  4.2.2. NetFlow

NetFlow technology is used to gather information about data flowing through a network, including who and what devices are in the network, and when and how users and devices access the network.

NetFlow is an important component in behavior-based detection and analysis. Switches, routers and firewalls equipped with NetFlow can report information about data entering, leaving and traveling through the network. 

This information is sent to NetFlow collectors that collect, store and analyze NetFlow data, which can be used to establish baseline behaviors on more than 90 attributes, such as source and destination IP address.

###  4.2.3 Penetration Testing

Penetration testing, commonly known as pen testing, is the act of assessing a computer system, network or organization for security vulnerabilities. A pen test seeks to breach systems, people, processes and code to uncover vulnerabilities which could be exploited. This information is then used to improve the system’s defenses to ensure that it is better able to withstand cyber attacks in the future.

Select the headings to explore the five-step pen test process.

> Step 1: Planning 

The pen tester gathers as much information as possible about a target system or network, its potential vulnerabilities and exploits to use against it. This involves conducting passive or active reconnaissance (footprinting) and vulnerability research.

> Step 2: Scanning 

The pen tester carries out active reconnaissance to probe a target system or network and identify potential weaknesses which, if exploited, could give an attacker access. Active reconnaissance may include:

* port scanning to identify potential access points into a target system
* vulnerability scanning to identify potential exploitable vulnerabilities of a particular target
* establishing an active connection to a target (enumeration) to identify the user account, system account and admin account.

> Step 3: Gaining Access 

The pen tester will attempt to gain access to a target system and sniff network traffic, using various methods to exploit the system including:

* launching an exploit with a payload onto the system
* breaching physical barriers to assets
* social engineering
* exploiting website vulnerabilities
* exploiting software and hardware vulnerabilities or misconfigurations
* breaching access controls security
* cracking weak encrypted Wi-Fi.

> Step 4: Maintain Access 

The pen tester will maintain access to the target to find out what data and systems are vulnerable to exploitation. It is important that they remain undetected, typically using backdoors, Trojan horses, rootkits and other covert channels to hide their presence.

When this infrastructure is in place, the pen tester will then proceed to gather the data that they consider valuable.

> Step 5: Analysis and Reporting 

The pen tester will provide feedback via a report that recommends updates to products, policies and training to improve an organization’s security.

###  4.2.4 Your Turn

You’ve been tasked with carrying out an internal pen test to check @Apollo’s computer network for vulnerabilities. How will you go about conducting your test? Get this right and earn some much needed defender points.

Great work! You have correctly identified how to carry out a pen test:

* Footprinting through the network to find ways to intrude gives you a chance to gather the information you need to plan a simulated attack.
* Scanning a target allows you to identify potential exploitable weaknesses.
* You will need to gain access to a network to exploit any vulnerabilities and simulate an attack.
* Maintaining access, without being detected, means that you can gather further information on a target’s vulnerabilities.
* Your findings will be reported to the organization so that security improvements can be made.

You have secured some defender points for @Apollo. Click on the shield icon in the top right-hand corner to check your progress.

###  4.2.5 Impact Reduction

While most organizations today are aware of common security threats and put considerable effort into preventing them, no set of security practices is foolproof. Therefore, organizations must be prepared to contain the damage if a security breach occurs. And they must act fast!

Don’t forget, the impact of a security breach extends beyond the technical aspect of stolen data or damaged intellectual property. It can have a devastating effect on an organization’s reputation!

###  4.2.6 What Is Risk Management?

Risk management is the formal process of continuously identifying and assessing risk in an effort to reduce the impact of threats and vulnerabilities. You cannot eliminate risk completely but you can determine acceptable levels by weighing up the impact of a threat with the cost of implementing controls to mitigate it. The cost of a control should never be more than the value of the asset you are protecting.

> Frame The Risk 

Identify the threats that increase risk. Threats may include processes, products, attacks, potential failure or disruption of services, negative perception of an organization’s reputation, potential legal liability or loss of intellectual property.

> Assess The Risk

Determine the severity that each threat poses. For example, some threats may have the potential to bring an entire organization to a standstill, while other threats may be only minor inconveniences. Risk can be prioritized by assessing financial impact (a quantitative analysis) or scaled impact on an organization's operation (a qualitative analysis).

> Respond to the risk

Develop an action plan to reduce overall organization risk exposure, detailing where risk can be eliminated, mitigated, transferred or accepted.

> Monitor the risk 

Continuously review any risk reduced through elimination, mitigation or transfer actions. Remember, not all risks can be eliminated, so you will need to closely monitor any threats that have been accepted.

 Next Up...

Cybersecurity expertise is in great demand. Most large organizations have dedicated Computer Security Incident Response Teams (CSIRT) to protect them from cyber attacks. Let’s take a look at how this works at Cisco.

Select Next to continue.

## 3. Cisco's Approach to Cybersecurity

Cybersecurity is becoming a significant business concern. Organizations should therefore have plans in place to prepare for, deal with, and recover from a security breach.

Here at @Apollo, we use Cisco technology. Let’s check these out.

###  4.3.1 Cisco's CSIRT

Many large organizations have a Computer Security Incident Response Team (CSIRT) to receive, review and respond to computer security incident reports. Cisco CSIRT goes a step further and provides proactive threat assessment, mitigation planning, incident trend analysis and security architecture review in an effort to prevent security incidents from happening.

Cisco’s CSIRT takes a proactive approach, collaborating with the Forum of Incident Response and Security Teams (FIRST), the National Safety Information Exchange (NSIE), the Defense Security Information Exchange (DSIE) and the DNS Operations Analysis and Research Center (DNS-OARC) to ensure we stay up-to-date with new developments.

There are several national and public CSIRT organizations, like the CERT Division of the Software Engineering Institute at Carnegie Mellon University, that are available to help organizations and national CSIRTs to develop, operate and improve their incident management capabilities.

###  4.3.2 Security Playbook

One of the best ways to prepare for a security breach is to prevent it. Organizations should provide guidance on:

* how to identify the cybersecurity risk to systems, assets, data and capabilities
* the implementation of safeguards and personnel training
* a flexible response plan that minimizes the impact and damage in the event of a security breach
* security measures and processes that need to be put in place in the aftermath of a security breach.

All this information should be compiled into a security playbook.

A security playbook is a collection of repeatable queries or reports that outline a standardized process for incident detection and response. Ideally, a security playbook should:

* highlight how to identify and automate the response to common threats such as the detection of malware-infected machines, suspicious network activity or irregular authentication attempts
* describe and clearly define inbound and outbound traffic
* provide summary information including trends, statistics and counts
* provide usable and quick access to key statistics and metrics
* correlate events across all relevant data sources.

###  4.3.3 Tools for Incident Detection and Prevention

There are a range of tools used to detect and prevent security incidents.

> SIEM 

A Security Information and Event Management (SIEM) system collects and analyzes security alerts, logs and other real-time and historical data from security devices on the network to facilitate early detection of cyber attacks.

> DLP

A Data Loss Prevention (DLP) system is designed to stop sensitive data from being stolen from or escaping a network. It monitors and protects data in three different states: data in use (data being accessed by a user), data in motion (data traveling through the network) and data at rest (data stored in a computer network or device).

Defining and implementing all of these various security policies can be time consuming and challenging. But Cisco has come up with a solution.

###  4.3.4 Cisco’s ISE and TrustSec

Cisco Identity Services Engine (ISE) and TrustSec enforce user access to network resources by creating role-based access control policies.

Press the play button to watch a short video and find out more about how this works.

###  4.3.5 Talk the Talk

This module contains a lot of technical information and jargon that you’ll need to know to develop your career in cybersecurity. So, before moving on, let’s check your understanding of some of these key terms. It’s your last chance to gain defender points, so think carefully before making your choices.

That’s right!

You have successfully matched each term to its description and gained some points that will help protect @Apollo from a cyber attack.

Remember:

* An IPS can block or deny traffic based on a positive rule or signature match.
* An IDS scans data against a database of rules or attack signatures, looking for malicious traffic.
* A DLP system is designed to stop sensitive data from being stolen from or escaping a network. 
* A SIEM system collects and analyzes security alerts, logs and other real-time and historical data from security devices on the network.

 Next Up...

Cybersecurity is critical for protecting all organizations, big and small, from cyber attacks and it can encompass a wide range of tools, structures, policies and processes.

You are making great progress but before you move on, let’s try a short quiz to check your understanding of all the information covered in this module.

## 4. Quiz

### Question 1

What name is given to a device that controls or filters traffic going in or out of the network?

### Question 2
This is a multiple choice question. Once you have selected an option, select the submit button below

'Today, there are single security appliances that will solve all the network security needs of an organization.'

Is this statement true or false?

### Question 3
This is a multiple choice question. Once you have selected an option, select the submit button below

What is the correct definition of risk management?

### Question 4
This is a multiple choice question. Once you have selected an option, select the submit button below

Which of the following tools can perform real-time traffic and port analysis, and can also detect port scans, fingerprinting and buffer overflow attacks?

### Question 5
This is a multiple choice question. Once you have selected an option, select the submit button below

What is the last stage of a pen test?

### Question 6
This is a multiple choice question. Once you have selected an option, select the submit button below

What protocol is used to collect information about traffic traversing a network?

### Question 7
Matching. Select from lists and then submit.

The risk management process consists of four steps. Can you put these in the right order?


