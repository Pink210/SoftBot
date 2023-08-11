# Discord token
token = ''

# Server and password of your server
server_pass = ["Server.xyz","password",]

# List of hubs and cascade and Country and server info and client info
'''
[Hub_Name] = The name of the hub
[Cascade_Name] = The name of the cascade
[Country] = The country where the hub is located.
[Server_Status] = The input to see the list of status off that server. like user type: ams and bot responed "Amesterdam is Online/Offline" [don't leave it empty and don't use the same]
[input_for_clients_of_Server] = The input to see the list of clients on that server [don't leave it empty and don't use the same]
'''
hub = [["Hub_Name","Cascade_Name","Country","Server_Status","*input_for_clients_of_Server"],
       ["Hub_Name2","Cascade_Name1","Country1","Server_Status1","*input_for_clients_of_Server"],
       ["Hub_Name3","Cascade_Name2","Country2","Server_Status2","*input_for_clients_of_Server"],
       ["Hub_Name4","Cascade_Name3","Country3","Server_Status3","*input_for_clients_of_Server"],
       ["Hub_Name5","Cascade_Name4","Country4","Server_Status4","*input_for_clients_of_Server"]]

# Discord channel you want bot to respond to 
channel_name = "test"

# Input for checking all server
all_server = "servers"

# Input for checking all client
all_client = "client"


# The hour, discord sends status of users and servers
timer = "8"

# Set the cooldown time in seconds (120 seconds = 2 minutes) for respons.
cooldown = "5"
