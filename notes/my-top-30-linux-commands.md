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
