# Discord Bot Project

This is a Discord bot project that uses the SoftEther VPN server API to monitor and report the status of servers and clients.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

To install and run this project, you need to have Python 3.9 or higher installed on your system. You also need to install the following Python packages:

- discord.py
- requests
- pandas

You can install them using pip:

```bash
pip install discord.py requests pandas
```

You also need to have a Discord account and create a bot token for your project. You can follow the instructions from [soon](^1^) to create a bot token.

You need to edit the setup.py file and enter the following information:

- Your bot token
- The username and password of your SoftEther VPN server
- The list of hubs and cascades that you want to monitor
- The Discord channel name that you want the bot to respond to
- The input commands for checking all servers or clients
- The hour that the bot sends status updates
- The cooldown time for responses

## Usage

To run the bot, you need to execute the main.py file:

```bash
python main.py
```

The bot will connect to your Discord server and start listening for messages in the specified channel. You can use the following commands to interact with the bot:

- Type the name of a server (e.g. `ams`) to get the status of that server (online or offline).
- Type the name of a client (e.g. `*ams`) to get information about clients on that server (name, expiry date, traffic).
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
['Turkey', 'Amsterdam', 'Germany2', 'Emarat']
or
Server is Offline
['English', 'Germany']
```
or
```text
Amsterdam is online
```
or
```text
User list of Amsterdam:
Name: user1 Expiry: 2023/12/31 Traffic: 1 GB
Name: user2 Expiry: No expiry Traffic: 2 GB
```



The bot will also send status updates every 8 hours (or as specified in the setup.py file) in the channel.

## Contribution

If you want to contribute to this project, you are welcome to do so. Please follow these steps:

- Fork this repository on GitHub.
- Clone your forked repository on your local machine.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with a clear message.
- Push your branch to your forked repository.
- Create a pull request from your branch to the main branch of this repository.
- Wait for feedback or approval.

Please follow the code style and format of this project. Also, please respect the code of conduct and be polite and constructive in your communication.

## Acknowledgements

This project was inspired by [this tutorial](https://www.youtube.com/@Indently) on how to create a Discord bot using Python. I also used [this documentation](https://github.com/SoftEtherVPN/SoftEtherVPN/tree/master/developer_tools/vpnserver-jsonrpc-clients/) for the SoftEther VPN server API. I would like to thank the authors of these resources for their helpful guidance.
