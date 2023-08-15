# Discord Bot Project

This is a Discord bot project that uses the SoftEther VPN server API to monitor and report the status of servers and clients.

## Table of Contents

- [Installation](#installation)
- [Configration](#configration)
- [What is this?](#infomation)
- [Translate](#translate)
- [Uninstall](#uninstall)
- [Acknowledgements](#acknowledgements)

## Installation

Automatically

<details>
  <summary>for Install & Update automatically</summary>

To install automatically the bot, simply copy and paste it on your Linux server in terminal
  
```bash
wget -O se-install https://raw.githubusercontent.com/Pink210/SoftBot/main/install.bash  && chmod +x se-install && ./se-install
```
</details>

Manually

<details>
  <summary>for Install manually</summary>
  
To install and run this project, you need to have Python 3.9 or higher installed on your system. You also need to install the following Python packages:
- discord.py
- discord.ext
- json
- time
- pandas

You can install them using pip:

```bash
pip install discord.py
pip install pandas
pip install json
pip install time
pip install discord.ext
```

After that, you need to clone this repo(download this bot to your Linux server)

```bash
git clone https://github.com/Pink210/SoftBot.git
```

Now is better to move it to the better location

```bash
cd ..
sudo mkdir /bot/
```
```bash
sudo cp -rf /root/SoftBot/ /bot/
```

Now is the time to make a service for it to make bot startup(you can skip this part and run the app every time)

```bash
sudo nano /etc/systemd/system/softbot.service
```

And pass this code to the file 

```bash
[Unit]
Description=SoftBot

[Service]
Type=simple
ExecStart=/usr/bin/python3 /bot/softbot/main.py
WorkingDirectory=/bot/softbot/
Restart=always

[Install]
WantedBy=sysinit.target
```
now running the service 

```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable SoftBot.service
```
```bash
sudo systemctl start SoftBot.service
```
If you don't want to have service You can run the bot with this code in the bot directory:

```bash
python main.py
```
THE END ;) NOW You need to edit the setup file for config the bot
</details>

## Configration

<details>
  <summary>for Setup and Configration</summary>

You need a Discord account and create a bot token for your project. You can follow the instructions from [here](https://discord.com/developers/docs/getting-started) to create a bot token.

You need to edit the setup.py file and enter the following information:

- Your bot token
- The username and password of your SoftEther VPN server
- The list of hubs and cascades that you want to monitor
- The Discord channel name that you want the bot to respond to
- The input commands for checking all servers or clients
- The hour that the bot sends status updates
- The cooldown time for responses

```bash
sudo nano /bot/SoftBot/setup.py
```
after that

```bash
sudo systemctl restart SoftBot.service
```

</details>

## Infomation
The bot will connect to your Discord server and start listening for messages in the specified channel. You can use the following commands to interact with the bot:

- Type the name of a server (e.g. `hubnumber1`) to get the status of that server (online or offline).
- Type the name of a client (e.g. `*hubnumber1`) to get information about clients on that server (name, expiry date, traffic).
- Type `servers` to get the status of all servers.
- Type `client` to get information about clients on all servers.

The bot will respond with a formatted message containing the requested information. For example:

```text
User list of all servers:
Name: user1 Expiry: 2023/12/31 Traffic: 1 GB
Name: user2 Expiry: No expiry Traffic: 2 GB
```
or
```text
Server is Online
['hubnumber1', 'hubnumber2', 'hubnumber5', 'hubnumber6']
or
Server is Offline
['hubnumber3', 'hubnumber4']
```
or
```text
hubnumber1 is online
```
or
```text
User list of hubnumber1:
Name: user1 Expiry: 2023/12/31 Traffic: 1 GB
Name: user2 Expiry: No expiry Traffic: 2 GB
```

The bot will also send status updates every 8 hours (or as specified in the setup.py file) in the channel.


## Translate

<details>
  <summary>Click here for details</summary>

```bash
sudo nano /bot/SoftBot/msg.py
```
You may translate the message into any language or format you like. 

</details>

## Uninstall

<details>
  <summary>Click here for details</summary>

```bash
wget -O se-install https://raw.githubusercontent.com/Pink210/SoftBot/main/uninstall.bash  && chmod +x se-install && ./se-install
```

</details>

## Acknowledgements

This project was inspired by [this tutorial](https://www.youtube.com/@Indently) on how to create a Discord bot using Python. I also used [this documentation](https://github.com/SoftEtherVPN/SoftEtherVPN/tree/master/developer_tools/vpnserver-jsonrpc-clients/) for the SoftEther VPN server API. I would like to thank the authors of these resources for their helpful guidance.
