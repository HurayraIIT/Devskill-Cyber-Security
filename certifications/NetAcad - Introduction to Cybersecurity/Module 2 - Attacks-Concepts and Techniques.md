# Module 2: Attacks, Concepts and Techniques 

Welcome to this module, which will explore the different methods that cybercriminals use to launch an attack.

Understanding what these are and how they work is the best way to protect ourselves. So, let’s make sure you know what you’re up against.

## 1. Analyzing a Cyber Attack

### 2.1.1 Types of Malware 

Cybercriminals use many different types of malicious software, or malware, to carry out their activities. Malware is any code that can be used to steal data, bypass access controls, or cause harm to or compromise a system. Knowing what the different types are and how they spread is key to containing and removing them.

Select the headings to find out more about some of the most common malware.

* Spyware:

Designed to track and spy on you, spyware monitors your online activity and can log every key you press on your keyboard, as well as capture almost any of your data, including sensitive personal information such as your online banking details. Spyware does this by modifying the security settings on your devices.

It often bundles itself with legitimate software or Trojan horses.

* Adware:

Adware is often installed with some versions of software and is designed to automatically deliver advertisements to a user, most often on a web browser. You know it when you see it! It’s hard to ignore when you’re faced with constant pop-up ads on your screen.

It is common for adware to come with spyware.

* Backdoor:

Adware is often installed with some versions of software and is designed to automatically deliver advertisements to a user, most often on a web browser. You know it when you see it! It’s hard to ignore when you’re faced with constant pop-up ads on your screen.

It is common for adware to come with spyware.

* Ransomware:

This malware is designed to hold a computer system or the data it contains captive until a payment is made. Ransomware usually works by encrypting your data so that you can’t access it.

Some versions of ransomware can take advantage of specific system vulnerabilities to lock it down. Ransomware is often spread through phishing emails that encourage you to download a malicious attachment or through a software vulnerability.

* Scareware:

This is a type of malware that uses 'scare’ tactics to trick you into taking a specific action. Scareware mainly consists of operating system style windows that pop up to warn you that your system is at risk and needs to run a specific program for it to return to normal operation.

If you agree to execute the specific program, your system will become infected with malware.

* Rootkit:

This malware is designed to modify the operating system to create a backdoor, which attackers can then use to access your computer remotely. Most rootkits take advantage of software vulnerabilities to gain access to resources that normally shouldn’t be accessible (privilege escalation) and modify system files.

Rootkits can also modify system forensics and monitoring tools, making them very hard to detect. In most cases, a computer infected by a rootkit has to be wiped and any required software reinstalled.

* Virus: 

A virus is a type of computer program that, when executed, replicates and attaches itself to other executable files, such as a document, by inserting its own code. Most viruses require end-user interaction to initiate activation and can be written to act on a specific date or time.

Viruses can be relatively harmless, such as those that display a funny image. Or they can be destructive, such as those that modify or delete data.

Viruses can also be programmed to mutate in order to avoid detection. Most viruses are spread by USB drives, optical disks, network shares or email.

* Trojan horse:

This malware carries out malicious operations by masking its true intent. It might appear legitimate but is, in fact, very dangerous. Trojans exploit your user privileges and are most often found in image files, audio files or games.

Unlike viruses, Trojans do not self-replicate but act as a decoy to sneak malicious software past unsuspecting users.

* Worms: 

This is a type of malware that replicates itself in order to spread from one computer to another. Unlike a virus, which requires a host program to run, worms can run by themselves. Other than the initial infection of the host, they do not require user participation and can spread very quickly over the network.

Worms share similar patterns: They exploit system vulnerabilities, they have a way to propagate themselves, and they all contain malicious code (payload) to cause damage to computer systems or networks.

Worms are responsible for some of the most devastating attacks on the Internet. In 2001, the Code Red worm had infected over 300,000 servers in just 19 hours.

### 2.1.2 Symptoms of Malware 

So now you know about the different kinds of malware. But what do you think their symptoms might be?

Take a pause and see what you can come up with, and when you’re ready, select the image to reveal some possible answers.

Regardless of the type of malware a system has been infected with, there are some common symptoms to look out for. These include:

* an increase in central processing unit (CPU) usage, which slows down your device
* your computer freezing or crashing often
* a decrease in your web browsing speed
* unexplainable problems with your network connections
* modified or deleted files
* the presence of unknown files, programs or desktop icons
* unknown processes running
* programs turning off or reconfiguring themselves
* emails being sent without your knowledge or consent.

This is exactly what could be happening at @Apollo!

Based on what you now know, do you think you could spot the different types of malware from their descriptions?

Let’s see!

### 2.1.3 What Do You Think? 

Match each of the descriptions to the correct malware type by selecting an answer from each dropdown, then Submit.

Remember:

* Spyware is designed to track and spy on you.
* Adware is designed to automatically deliver advertisements to a user.
* Worms replicate themselves in order to spread from one computer to another.
* Viruses replicate and attach to other executable files by inserting their own code.
* Ransomware is designed to hold a computer system or the data it contains captive until a payment is made.

 Next Up...

There are many different malware types that pose a threat to your organization but how can cybercriminals get into your networks and systems in the first place? They have many means at their disposal.

Select Next to continue.

## 2. Methods of Infiltration

### 2.2.1 Social Engineering

Social engineering is the manipulation of people into performing actions or divulging confidential information. Social engineers often rely on people’s willingness to be helpful, but they also prey on their weaknesses. For example, an attacker will call an authorized employee with an urgent problem that requires immediate network access and appeal to the employee’s vanity or greed or invoke authority by using name-dropping techniques in order to gain this access.

> Pretexting

This is when an attacker calls an individual and lies to them in an attempt to gain access to privileged data.

For example, pretending to need a person’s personal or financial data in order to confirm their identity.

> Tailgating

This is when an attacker quickly follows an authorized person into a secure, physical location.

> Something for something (quid pro quo)

This is when an attacker requests personal information from a person in exchange for something, like a free gift.

### 2.2.2 Denial-of-Service 

Denial-of-Service (DoS) attacks are a type of network attack that is relatively simple to carry out, even by an unskilled attacker. A DoS attack results in some sort of interruption of network service to users, devices or applications.

> Overwhelming quantity of traffic

This is when a network, host or application is sent an enormous amount of data at a rate which it cannot handle. This causes a slowdown in transmission or response, or the device or service to crash.

> Maliciously formatted packets

A packet is a collection of data that flows between a source and a receiver computer or application over a network, such as the Internet. When a maliciously formatted packet is sent, the receiver will be unable to handle it.

For example, if an attacker forwards packets containing errors or improperly formatted packets that cannot be identified by an application, this will cause the receiving device to run very slowly or crash.

DoS attacks are considered a major risk because they can easily interrupt communication and cause significant loss of time and money.

### 2.2.3 Distributed DoS 

A Distributed DoS (DDoS) attack is similar to a DoS attack but originates from multiple, coordinated sources. For example:

* An attacker builds a network (botnet) of infected hosts called zombies, which are controlled by handler systems.
* The zombie computers will constantly scan and infect more hosts, creating more and more zombies.
* When ready, the hacker will instruct the handler systems to make the botnet of zombies carry out a DDoS attack.

### 2.2.4 Botnet 

A bot computer is typically infected by visiting an unsafe website or opening an infected email attachment or infected media file. A botnet is a group of bots, connected through the Internet, that can be controlled by a malicious individual or group. It can have tens of thousands, or even hundreds of thousands, of bots that are typically controlled through a command and control server.

These bots can be activated to distribute malware, launch DDoS attacks, distribute spam email, or execute brute-force password attacks. Cybercriminals will often rent out botnets to third parties for nefarious purposes.

Many organizations. like Cisco, force network activities through botnet traffic filters to identify any botnet locations.

* Infected bots try to communicate with a command and control host on the Internet.
* The Cisco Firewall botnet filter is a feature that detects traffic coming from devices infected with the malicious botnet code.
* The cloud-based Cisco Security Intelligence Operations (SIO) service pushes down updated filters to the firewall that match traffic from new known botnets.
* Alerts go out to Cisco’s internal security team to notify them about the infected devices that are generating malicious traffic so that they can prevent, mitigate and remedy these.

### 2.2.5 On-Path Attacks 

On-path attackers intercept or modify communications between two devices, such as a web browser and a web server, either to collect information from or to impersonate one of the devices.

This type of attack is also referred to as a man-in-the-middle or man-in-the-mobile attack.

A MitM attack happens when a cybercriminal takes control of a device without the user’s knowledge. With this level of access, an attacker can intercept and capture user information before it is sent to its intended destination. These types of attacks are often used to steal financial information.

There are many types of malware that possess MitM attack capabilities.

A variation of man-in-middle, MitMo is a type of attack used to take control over a user’s mobile device. When infected, the mobile device is instructed to exfiltrate user-sensitive information and send it to the attackers. ZeuS is one example of a malware package with MitMo capabilities. It allows attackers to quietly capture two-step verification SMS messages that are sent to users.

There are a lot of ways for cybercriminals to infiltrate your systems and networks, but it’s important that you know what these are.

Let’s keep going!

### 2.2.6 SEO Poisoning

You’ve probably heard of search engine optimization or SEO which, in simple terms, is about improving an organization’s website so that it gains greater visibility in search engine results.

So what do you think SEO poisoning might be? Take a moment to consider this and when you’re ready, select the image to find out if you were right!

Search engines such as Google work by presenting a list of web pages to users based on their search query. These web pages are ranked according to the relevancy of their content.

While many legitimate companies specialize in optimizing websites to better position them, attackers take advantage of popular search terms and use SEO to push malicious sites higher up the ranks of search results. This technique is called SEO poisoning.

The most common goal of SEO poisoning is to increase traffic to malicious sites that may host malware or attempt social engineering.

### 2.2.7 Wi-Fi Password Cracking 

You’re enjoying your lunch in the canteen when a colleague approaches you. They seem distressed.

They explain that they can’t seem to connect to the public Wi-Fi on their phone and ask if you have the private Wi-Fi password to hand so that they can check that their phone is working.

How would you respond?

This colleague could be carrying out a social engineering attack, manipulating you to provide the password used to protect the organization’s private wireless network. You can never be too careful – and, for answering correctly, you’ve earned some defender points. Well done!

Hackers have other techniques up their sleeves. Some use brute-force attacks, testing possible password combinations to try and guess a password. Others are able to identify unencrypted passwords by listening in and capturing packets sent on the network. This is called network sniffing. If the password is encrypted, they may still be able to reveal it using a password cracking tool.

### 2.2.8 Password Attacks 

Entering a username and password is one of the most popular forms of authenticating to a web site. Therefore, uncovering your password is an easy way for cybercriminals to gain access to your most valuable information.

> Password Spraying

This technique attempts to gain access to a system by ‘spraying’ a few commonly used passwords across a large number of accounts. For example, a cybercriminal uses 'Password123' with many usernames before trying again with a second commonly-used password, such as ‘qwerty.’

This technique allows the perpetrator to remain undetected as they avoid frequent account lockouts.

> Dictionary attacks

A hacker systematically tries every word in a dictionary or a list of commonly used words as a password in an attempt to break into a password-protected account.

> Brute-force attacks

The simplest and most commonly used way of gaining access to a password-protected site, brute-force attacks see an attacker using all possible combinations of letters, numbers and symbols in the password space until they get it right.

> Rainbow attacks

Passwords in a computer system are not stored as plain text, but as hashed values (numerical values that uniquely identify data). A rainbow table is a large dictionary of precomputed hashes and the passwords from which they were calculated.

Unlike a brute-force attack that has to calculate each hash, a rainbow attack compares the hash of a password with those stored in the rainbow table. When an attacker finds a match, they identify the password used to create the hash.

> Traffic interception

Plain text or unencrypted passwords can be easily read by other humans and machines by intercepting communications.

If you store a password in clear, readable text, anyone who has access to your account or device, whether authorized or unauthorized, can read it.

### 2.2.9 Cracking Times 

It looks as if the hackers are trying everything to crack @Apollo’s private Wi-Fi password. We have to make sure that the password is strong enough to withstand their attack!

Take a look at the following passwords. Click the numbers to put them in the correct order according to how long you think it would take an attacker to crack each one using brute-force, where 1 is the shortest amount of time and 4, the highest.

Let's recap the steps involved in carrying out a pen test:

* Planning allows you to gather as much information as possible about a target system or network and may involve passive or active reconnaissance (footprinting).
* Scanning a target allows you to identify potential exploitable weaknesses.
* You will need to gain access to a network to exploit any vulnerabilities and simulate an attack.
* Maintaining access, without being detected, means that you can gather further information on a target’s vulnerabilities.
* You will report any feedback to the organization so that security improvements can be made.

Go back, reset and try again. Remember, there are defender points to be won!

Great work! You have correctly identified how to carry out a pen test:

* Footprinting through the network to find ways to intrude gives you a chance to gather the information you need to plan a simulated attack.
* Scanning a target allows you to identify potential exploitable weaknesses.
* You will need to gain access to a network to exploit any vulnerabilities and simulate an attack.
* Maintaining access, without being detected, means that you can gather further information on a target’s vulnerabilities.
* Your findings will be reported to the organization so that security improvements can be made.

You have secured some defender points for @Apollo. Click on the shield icon in the top right-hand corner to check your progress.

### 2.2.10 Advanced Persistent Threats 

Attackers also achieve infiltration through advanced persistent threats (APTs) — a multi-phase, long term, stealthy and advanced operation against a specific target. For these reasons, an individual attacker often lacks the skill set, resources or persistence to perform APTs.

Due to the complexity and the skill level required to carry out such an attack, an APT is usually well-funded and typically targets organizations or nations for business or political reasons.

Its main purpose is to deploy customized malware on one or more of the target’s systems and remain there undetected.

### 2.2.11 It’s Over to You... 

Phew! That’s a lot to take in and hackers certainly have a lot of tools at their disposal. It is important that you know what these are so that you can protect yourself and @Apollo.

You think back to some of the suspicious activities that you’ve seen recently in the organization. Based on what you have learned in this topic, what type of attack could each of these scenarios be? Take your time with this one. You have a chance to earn some much-needed defender points.

You were able to identify the potential attacks that could be happening right under your nose. Remember, it’s important to stay alert and be mindful of all of the ways that attackers are trying to catch you out. Bear in mind that many modern attacks involve a blend of these methods, with cybercriminals often using multiple techniques to infiltrate and attack a system.

 Next Up...

In order to prevent cybercriminals from launching a cyber attack, organizations need to be constantly checking for security vulnerabilities in their systems and networks.

Select Next to continue.

## 3. Security Vulnerability and Exploits

Before we get into the details, let’s start by outlining some key terms that you need to know.

Security vulnerabilities are any kind of software or hardware defect. A program written to take advantage of a known vulnerability is referred to as an exploit. A cybercriminal can use an exploit against a vulnerability to carry out an attack, the goal of which is to gain access to a system, the data it hosts or a specific resource.

###  2.3.1 Hardware Vulnerabilities

Hardware vulnerabilities are most often the result of hardware design flaws. For example, the type of memory called RAM basically consists of lots of capacitors (a component which can hold an electrical charge) installed very close to one another. However, it was soon discovered that, due to their close proximity, changes applied to one of these capacitors could influence neighbor capacitors. Based on this design flaw, an exploit called Rowhammer was created. By repeatedly accessing (hammering) a row of memory, the Rowhammer exploit triggers electrical interferences that eventually corrupt the data stored inside the RAM.

**Meltdown and Spectre**

Google security researchers discovered Meltdown and Spectre, two hardware vulnerabilities that affect almost all central processing units (CPUs) released since 1995 within desktops, laptops, servers, smartphones, smart devices and cloud services.

Attackers exploiting these vulnerabilities can read all memory from a given system (Meltdown), as well as data handled by other applications (Spectre). The Meltdown and Spectre vulnerability exploitations are referred to as side-channel attacks (information is gained from the implementation of a computer system). They have the ability to compromise large amounts of memory data because the attacks can be run multiple times on a system with very little possibility of a crash or other error.

Hardware vulnerabilities are specific to device models and are not generally exploited through random compromising attempts. While hardware exploits are more common in highly targeted attacks, traditional malware protection and good physical security are sufficient protection for the everyday user.

### 2.3.2 Software Vulnerabilities 

Software vulnerabilities are usually introduced by errors in the operating system or application code.

Select the logo to find out more about the SYNful Knock vulnerability discovered in Cisco Internetwork Operating System (IOS) in 2015.

The SYNful Knock vulnerability allowed attackers to gain control of enterprise-grade routers, such as the legacy Cisco ISR routers, from which they could monitor all network communication and infect other network devices.

This vulnerability was introduced into the system when an altered IOS version was installed on the routers. To avoid this, you should always verify the integrity of the downloaded IOS image and limit the physical access of such equipment to authorized personnel only.

### 2.3.3 Categorizing Software Vulnerabilities

Most software security vulnerabilities fall into several main categories.

> Buffer overflow

Buffers are memory areas allocated to an application. A vulnerability occurs when data is written beyond the limits of a buffer. By changing data beyond the boundaries of a buffer, the application can access memory allocated to other processes. This can lead to a system crash or data compromise, or provide escalation of privileges.

> Non-validated input

Programs often require data input, but this incoming data could have malicious content, designed to force the program to behave in an unintended way.

For example, consider a program that receives an image for processing. A malicious user could craft an image file with invalid image dimensions. The maliciously crafted dimensions could force the program to allocate buffers of incorrect and unexpected sizes.

> Race conditions

This vulnerability describes a situation where the output of an event depends on ordered or timed outputs. A race condition becomes a source of vulnerability when the required ordered or timed events do not occur in the correct order or at the proper time.

> Weaknesses in security practices

Systems and sensitive data can be protected through techniques such as authentication, authorization and encryption. Developers should stick to using security techniques and libraries that have already been created, tested and verified and should not attempt to create their own security algorithms. These will only likely introduce new vulnerabilities.

> Access control problems

Access control is the process of controlling who does what and ranges from managing physical access to equipment to dictating who has access to a resource, such as a file, and what they can do with it, such as read or change the file. Many security vulnerabilities are created by the improper use of access controls.

Nearly all access controls and security practices can be overcome if an attacker has physical access to target equipment. For example, no matter the permission settings on a file, a hacker can bypass the operating system and read the data directly off the disk. Therefore, to protect the machine and the data it contains, physical access must be restricted, and encryption techniques must be used to protect data from being stolen or corrupted.

### 2.3.4 Software Updates 

The goal of software updates is to stay current and avoid exploitation of vulnerabilities. Microsoft, Apple and other operating system producers release patches and updates almost every day and applications such as web browsers, mobile apps and web servers are often updated by the companies or organizations responsible for them.

Despite the fact that organizations put a lot of effort into finding and patching software vulnerabilities, new vulnerabilities are discovered regularly. That’s why some organizations use third party security researchers who specialize in finding vulnerabilities in software, or actually invest in their own penetration testing teams dedicated to search, find and patch software vulnerabilities before they can get exploited.

Google’s Project Zero is a great example of this practice. After discovering a number of vulnerabilities in various software used by end users, Google formed a permanent team dedicated to finding software vulnerabilities. You can find out more about Google’s security research here.

### 2.3.5 What Do You Think? 

This has made you think about some of the vulnerabilities that may exist at @Apollo. After some investigation you’ve noted some potential issues.

Can you identify what category each of these vulnerabilities falls into? You have a chance to earn some defender points here and further safeguard @Apollo, so take your time.

Let's recap!

* Access control problems occur through the improper use of practices that manage physical control of equipment, data or applications.
* Weaknesses in security practices exist when systems and sensitive data are not protected through techniques such as authentication, authorization and encryption.
* A non-validated input describes a vulnerability in which data supplied to a program by a user or exploit causes the application to behave in an unintended way.

Go back, reset and try again.

That’s right! Great work!

You’ve correctly identified the potential security issues and have taken a step closer to safeguarding @Apollo from attack. Remember:

* Emailing sensitive information such as passwords in plain text is extremely risky and is a weakness in security practice. This information should at the very least be encrypted.
* Past employees should not have access to customer information when leaving a company. This is a serious access control problem.
* New users need to be validated before anything else can be done with their data. Using an incorrectly formatted email address to log on is a non-validated input error.

Check your progress by clicking on the shield icon in the top right hand corner of your screen.

 Next Up...

You need to be constantly aware of security vulnerabilities around you so that you can respond accordingly. But remember, the cybersecurity landscape is continually evolving. For example, cryptojacking — a type of cyber attack used to mine cryptocurrency — is on the rise.

## 4. The Cybersecurity Landscape

You’ve likely heard of cryptocurrency, but do you know exactly what it is and how it works?

### 2.4.1 Cryptocurrency 

Cryptocurrency is digital money that can be used to buy goods and services, using strong encryption techniques to secure online transactions. Banks, governments and even companies like Microsoft and AT&T are very aware of its importance and are jumping on the cryptocurrency bandwagon!

Cryptocurrency owners keep their money in encrypted, virtual ‘wallets.’ When a transaction takes place between the owners of two digital wallets, the details are recorded in a decentralized, electronic ledger or blockchain system. This means it is carried out with a degree of anonymity and is self-managed, with no interference from third parties such as central banks or government entities.

Approximately every ten minutes, special computers collect data about the latest cryptocurrency transactions, turning them into mathematical puzzles to maintain confidentiality.

These transactions are then verified through a technical and highly complex process known as ‘mining.’ This step typically involves an army of ‘miners’ working on high-end PCs to solve mathematical puzzles and authenticate transactions.

Once verified, the ledger is updated and electronically copied and disseminated worldwide to anyone belonging to the blockchain network, effectively completing a transaction.

### 2.4.2 Cryptojacking 

Cryptojacking is an emerging threat that hides on a user’s computer, mobile phone, tablet, laptop or server, using that machine’s resources to 'mine’ cryptocurrencies without the user's consent or knowledge.

Many victims of cryptojacking didn’t even know they’d been hacked until it was too late!

 Next Up...

It’s clear that the cyber landscape is changing. And while the rise of cryptocurrency has produced lots of opportunity, it also exposes more vulnerabilities, making it easier than ever before for hackers to steal huge sums of money online.

You’re almost at the end of this module. But before you go, let’s check your knowledge with a short quiz.

Select Next to continue.

## 5. Quiz

The following quiz is based on what you have just learned. There are eight questions in total and you need to score at least 70% in order to pass.

Good luck!

Question 1

Which of the following examples illustrates how malware might be concealed?

Question 2

What is the purpose of a rootkit?

Question 3

What type of attack allows an attacker to use a brute-force approach?

Question 4

What is the most common goal of search engine optimization (SEO) poisoning?

Question 5

A set of changes done to any program or application with the aim of updating, fixing or improving it is often referred to as what?

Question 6

Which of the following should be carried out to address known software vulnerabilities of a specific application?

Question 7

Which of the following security vulnerabilities could result in the receipt of malicious information that could force a program to behave in an unintended way?

Question 8

What is a miner?
