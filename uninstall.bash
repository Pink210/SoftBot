#!/usr/bin/env bash
(( EUID != 0 )) && exec sudo -- "$0" "$@"
red='\033[0;31m'
clear

read -rep $'!!! IMPORTANT !!!\n\nAre you certain you want to get rid of SoftBot? :( [[y/N]] ' response
case "$response" in
[yY][eE][sS]|[yY])

clear
echo -e "${red}'Sad to See You GO ;( ' ${plain}"


if [ -d "/bot/SoftBot" ]; 
then
  echo "${red}Uninstalling ...${plain}"
  sudo systemctl stop softbot
  sleep 2
  sudo rm -rf /bot/SoftBot
  sudo systemctl disable softbot
  sudo rm /etc/systemd/system/softbot.service
  sudo systemctl daemon-reload
  echo -e "${red}'Uninstall Complete. Im sorry. Next time i try to be better bot ' ${plain}"
else 
"${red}SoftBot in not installed on this server.${plain}"
fi

clear
