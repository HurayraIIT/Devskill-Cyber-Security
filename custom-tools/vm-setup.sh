: '
  Everytime I setup a linux machine or create a cloud vm instance, I need to do some initial setup every time. I will try to automate the steps using this script. This will be fun inShaAllah.
'

# Begin
echo "Hello Boss. Good morning!";

# System update
sudo apt update
sudo apt upgrade -y

# Install basic tools
sudo apt install -y neofetch vim gcc g++ net-tools rar unrar p7zip-full p7zip-rar python3-pip nmap ncdu nnn openjdk-11-jdk 

sudo snap install btop

# Finish
sudo apt autoremove -y
clear

whoami
pwd
neofetch 
