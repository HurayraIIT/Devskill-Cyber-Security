: '
  Everytime I setup a linux machine or create a cloud vm instance, I need to do some initial setup every time. I will try to automate the steps using this script. This will be fun inShaAllah.
'

# Begin
echo "Hello Boss. Good morning!";

# System update
sudo apt update
sudo apt upgrade -y

# Install basic tools
sudo apt install neofetch vim gcc g++ net-tools p7zip-full

# Finish
whoami
pwd
neofetch 
