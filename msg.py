# All BOT massege is here if you want to translate it or change it[ BE CAREFUL! ]

# Prints the status of one server
"""
    Sends a response to the user's message for one server status be like:
    user typing Germany and bot respance: Germany Server is Online/Offline.
"""
server_online = "Server is Online"
server_offline = "Server is Offline"

# Prints the status of all servers
"""
    Sends a response to the user's message for all server status be like:
    List of Online Servers: 
    [Server One , Server Two]
    List of Offline Servers: 
    [Server Three]
"""
list_online_servers = "List of Online Servers: "
list_offline_servers = "List of Offline Servers: "
"""
    Sends a response to the user's message for all server status be like:
    List of Online Servers: 
    [Server One , Server Two]
    List of Offline Servers: 
    [There are 'NO' Servers currently Offline.]
"""
no_online_servers = "There are 'NO' Servers currently Online."
no_offline_servers = "There are 'NO' Servers currently Offline."


#  Prints the client status in a specific server
"""
    Like This:
    User list of [Germany] Server
    user1 | no Expire | 200 GB
    user2 | no Expire | 200 GB
    [Germany] is name of server
"""
before_server_name = "User list of"
after_server_name = " Server:"

# Prints the client status in all servers
"""
    Like This:
    User list of all servers:
    user1 | no Expired | 200 GB
    user2 | no Expired | 200 GB
"""
list_users = "User list of all servers:"

"""
    Sends a response to the user's message for Clinet[All Servers and One servers] status be like:
    default is like this
    user1 | no Expired | 200 GB
    user2 | EX: 2000:01:01 | 200 GB
    [before_name][name][after_name][if user have no expire date][after_expire][before_trafic][after_trafic]
    USE AFTER_* FOR DIVIDED
    traffic is showing as GB so is better to use GB at [after_trafic]
"""
before_name = ""
after_name = " | "
before_expiry = "Expired Date: "
no_expiry_message = "Infinite"
after_expiry = " | "
before_traffic = ""
after_traffic = "GB"

#Message on cooldown
cooldown_message = "Give me a break while I relax."
