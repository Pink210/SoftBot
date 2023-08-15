#If you using a Linux nano editor follow this instruction 
'''
For Paste = Click right or Ctrl+U
for Cut\Delete = Ctrl+K
for saving = Ctrl+X => Y => Enter
if you using Windows you can edit this file and then select all code here Ctrl+K and past it here for easy solution. 
'''

# Discord token
token = ''

# Server and password of your server
server_pass = ["domain/IP", "pass"]

# List of hubs and cascade and Country and server info and client info
'''
[1] = The name of the hub
[2] = The name of the cascade
[3] = The name of VH for the bot.
[4] = The input to see the list of statuses of that server. like user types: "VHub1" and the bot responded VHub1 is Online/Offline" [don't leave it empty and don't use the same]
[5] = The input to see the list of clients on that server [don't leave it empty and don't use the same]
'''
hub = [["1", "2", "3", "4", "*5"],
       ["1", "2", "3", "4", "*5"],
       ["1", "2", "3", "4", "*5"],
       ["1", "2", "3", "4", "*5"],
       ["1", "2", "3", "4", "*5"]]

# Discord channel you want the bot to respond to 
channel_name = "test"

# Input for checking all server
all_server = "servers"

# Input for checking all client
all_client = "client"


# The hour, discord sends the status of users and servers
timer = "8"

# Set the cooldown time in seconds (120 seconds = 2 minutes) for respons.
cooldown = "5"
