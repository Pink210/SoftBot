#!/usr/bin/env bash
(( EUID != 0 )) && exec sudo -- "$0" "$@"
green=‘\033[0;32m’ yellow=‘\033[0;33m’ red=‘\033[0;31m’ plain=‘\033[0m’

clear

read -rep $'!!! IMPORTANT !!!\n\ngreendo you want continue? [[y/N]]{plain}' response
case "$response" in
[yY][eE][sS]|[yY])

# Check for the Update and make a backup
if [ -d "/bot/SoftBot" ]; then
  echo "${red}SoftBot is already installed. The script is attempting to create a backup."
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
sudo apt-get update -y && sudo apt-get -o Dpkg::Options::="--force-confold" -y upgrade -y && sudo apt-get autoremove -y 
sleep 2

# install necessary pip
apt install python3-pip -y
sleep 2
pip install discord.py
pip install discord 
pip install pandas
pip install json
pip install time
pip install discord.ext


# Download SoftBot
git clone https://github.com/Pink210/SoftBot.git || exit
sleep 2
cd .. || exit
sudo mkdir /bot/
sleep 2
sudo cp -rf /root/SoftBot/ /bot/
sleep 2

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

# Restore backup
if [ -d "/opt/backup" ]; then
  echo "Restoring backup."
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
echo 'Have FUN ;).'
echo 'First "sudo nano /bot/SoftBot/setup.py" for Config the bot'
echo 'second "sudo systemctl restart softbot.service" to run the bot'
