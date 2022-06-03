# My Top 30 Linux Commands

## ```ssh```
**Usage:** For secure communication with a remote host.

* To connect to a remote host as root:
```
ssh root@123.4.5.67
```

## ```adduser```
**Usage:** For creating a new user.

* To create a new user named **hurayra**:
```
adduser hurayra
``` 

* To add the user **hurayra** to sudo group:
```
adduser hurayra sudo
``` 

## ```usermod```
**Usage:** For modifying a user account.

* For adding the user **hurayra** to the sudo group:
```
usermod -aG sudo hurayra
``` 
## ```su```
**Usage:** For switching user.

* Switch to root user:
```
sudo su
``` 

* Switch to another user:
```
su hurayra
``` 

## ```passwd```
**Usage:** For changing password.

* To change a password for user named tom:
```
sudo passwd tom
``` 

* To change a password for root user:
```
sudo passwd root
``` 

* To change your own password:
```
passwd
```

## ```ufw```
**Usage:** uncomplicated firewall. For changing firewall settings.

* To check current ufw rules:
```
sudo ufw status verbose
``` 

* To enable ufw:
```
sudo ufw enable
``` 

* To disable ufw:
```
sudo ufw disable
``` 

* To block an ip address:
```
sudo ufw deny from 123.4.5.66
``` 

* To block an entire subnet:
```
sudo ufw deny from 203.0.113.0/24
```

* To delete ufw rule:
```
sudo ufw status numbered
sudo ufw delete 1
```

* To list available application profile:
```
sudo ufw app list
```

* To allow ssh:
```
sudo ufw allow OpenSSH
```

## ```sha256sum```

It can check the SHA 256 sum of a file. To see the sum:
```
sha256sum file.iso
```

## ```curl```

curl command can be used to communicate with a server. To see the HTTP response:
```
curl wpdeveloper.com
```

## ```wget```

To download a file:
```
wget https://golang.org/dl/go1.16.5.linux-amd64.tar.gz
```

## ```tar```

Tar can compress or extract archives in different format. To extract a tar gz file and throw it in a target directory:
```
tar -xzf go1.16.5.linux-amd64.tar.gz -C /usr/local
```

## ```zip```

To zip some files and folders:
```
zip -r output.zip file1 file2 folder1 folder2
```

## ```unzip```

To unzip a file and throw it in a target directory:
```
unzip file.zip -d /destination/directory
```

## ```mkdir```

To create a directory but ignore if the directory already exists:
```
mkdir -p dir1
```

## ```exit```

This command terminates a shell session and in some cases closes the terminal.

## ```shutdown```

This can half, power-off or reboot the machine.
* To power off the machine: `shutdown -P`
* To halt the machine: `shutdown -H`
* To reboot the machine: `shutdown -r`
* Shutdown at 15:06 : `shutdown 15:06`
* To cancel a scheduled shutdown: `shutdown -c`

## ```ps```

This can be used to see the running processes on the machine.

## ```kill```

Kills a running process.
```
kill <pid>
```

## ```which```

This command outputs the path of shell command binaries: `which python`

## ```shred```

Corrupt or overwrite the contents of a file to make it difficult to recover: `shred file.txt`
To delete the file after overwriting: `shred -u file.txt`

## ```tail```

To see the last n lines of a file:
```
tail -n 20 file.txt
```

## ```head```

To see the first n lines of a file:
```
head -n 20 file.txt
```

## ```whatis```

Prints a single line reference of a command:
```
whatis python
```

## ```wc```

To see the word count of a file: `wc -w file.txt`

## ```uname```

To see the OS information: `uname -a`

## ```df```

To report file system disk space usage: `df`

## ```traceroute```

To trace the route to a host: `traceroute wpdeveloper.com`

## ```rm```

To remove files and folders: `rm -r folder1`

## ```history```

To see the command history: `history`

## ```sort```

This command sorts the results of a search either alphabetically or numerically. It also sorts files, file contents, and directories. 
```
sort file.txt
```

## ```diff```

To find difference between 2 files:
```
diff file1 file2
```