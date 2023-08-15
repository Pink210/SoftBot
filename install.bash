#!/usr/bin/env bash
(( EUID != 0 )) && exec sudo -- "$0" "$@"
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
plain='\033[0m'

clear

echo -e "${yellow}'hello' ${plain}"


# Check for the Update and make a backup
if [ -d "/bot/SoftBot" ]; then
  echo "${green}SoftBot is already installed. The script is attempting to create a backup.${plain}"
  echo "USE 'Ctrl + C' to cancel it."
  sudo systemctl stop softbot
  sleep 2
  sudo mkdir /bot/backup
  sleep 2
  sudo cp -f /bot/softether/msg.py /bot/backup/msg.py.bak
  sleep 2
  sudo cp -f /bot/softether/setup.py /bot/backup/setup.py.bak
  sleep 2
  sudo systemctl disable softbot
fi

# Start from here
# Perform apt update
echo "${green}Updating Linux${plain}"
sudo apt-get update -y && sudo apt-get -o Dpkg::Options::="--force-confold" -y upgrade -y && sudo apt-get autoremove -y 
sleep 2
clear
echo "${green}installing PIP${plain}"
# install the necessary pip
apt install python3-pip -y || exit
sleep 2
pip install discord.py  || exit
pip install discord  || exit
pip install pandas  || exit
pip install discord.ext
echo "${red}IGNORE the error${plain}"
pip install json
pip install time


clear
echo "${green}So far so good${plain}"
echo "${green}Download the bot${plain}"
# Download SoftBot
git clone https://github.com/Pink210/SoftBot.git || exit
sleep 2
cd .. || exit
sudo mkdir /bot/
sleep 2
sudo cp -rf /root/SoftBot/ /bot/
sleep 2

echo "${green}Create the service${plain}"
# Create the service file with the desired content
sudo tee /etc/systemd/system/softbot.service > /dev/null << 'EOF'
[Unit]
Description=SoftBot

[Service]
Type=simple
ExecStart=/usr/bin/python3 /bot/SoftBot/main.py
WorkingDirectory=/bot/SoftBot/
Restart=always

[Install]
WantedBy=sysinit.target
EOF
sleep 2
# Reload the systemd daemon to recognize the new service
sudo systemctl daemon-reload
sleep 2
# Enable the service to start on boot
sudo systemctl enable softbot.service || exit
sleep 3
# Start the service
sudo systemctl start softbot.service || exit
sleep 2
sudo systemctl stop softbot.service

clear
# Restore backup
if [ -d "/opt/backup" ]; then
  echo "${green}Restoring backup.${plain}"
  sudo systemctl stop softbot.service
  sleep 2
  sudo cp -f /bot/backup/msg.py.bak /bot/softether/msg.py 
  sleep 2
  sudo cp -f /bot/backup/setup.py.bak /bot/softether/setup.py 
  sudo systemctl restart softbot.service
fi

#add needrestart back again
sudo sed -i "s/#\$nrconf{restart} = 'a';/\$nrconf{restart} = 'i';/" /etc/needrestart/needrestart.conf
clear
echo "${green}Have FUN ;).${plain}"
echo "${red}First 'sudo nano /bot/SoftBot/setup.py' for Config the bot${plain}"
echo "${red}then 'sudo systemctl restart softbot.service' to run the bot${plain}"
