# Discord token
token = ''

# Server and password of your server
server_pass = ["Server.com", "password"]

# List of hubs and cascade and Country and server info and client info
'''
[Hub_Name] = The name of the hub
[Cascade_Name] = The name of the cascade
[hubname] = The name of VH for the bot.
[Server_Status] = The input to see the list of statuses off that server. like user types: "VHub1" and the bot responded VHub1 is Online/Offline" [don't leave it empty and don't use the same]
[input_for_clients_of_Server] = The input to see the list of clients on that server [don't leave it empty and don't use the same]
'''
hub = [["Hub_Name","Cascade_Name","hubname","Server_Status","*input_for_clients_of_Server"],
       ["Hub_Name2","Cascade_Name1","hubname","Server_Status1","*input_for_clients_of_Server"],
       ["Hub_Name3","Cascade_Name2","hubname","Server_Status2","*input_for_clients_of_Server"],
       ["Hub_Name4","Cascade_Name3","hubname","Server_Status3","*input_for_clients_of_Server"],
       ["Hub_Name5","Cascade_Name4","hubname","Server_Status4","*input_for_clients_of_Server"]]

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
