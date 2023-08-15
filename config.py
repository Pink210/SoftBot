# Import the Json and pandas for interact with Softether API.
import json
import pandas as pd

# Import the requests, setup, and message modules from local files.
import requests
import setup
import msg


# Set up server, API site, and password
server = setup.server_pass[0]
apisite = f"https://{server}:5555/api/"
password = setup.server_pass[1]

# Leave username empty as SoftEther does not have a username
username = ""

def SendCommand(gateway, password, method, params):
    """
    Send a command to the SoftEther VPN server.
    :param gateway: The URL of the SoftEther VPN server.
    :param password: The password for the SoftEther VPN server.
    :param method: The method to be called on the SoftEther VPN server.
    :param params: The parameters for the method being called.
    :return: The result of the command or False if an error occurred.
    """
    try:
        # Set up the payload for the request
        payload = {
            "jsonrpc": "2.0",
            "id": "rpc_call_id",
            "method": method,
            "params": params
        }
        headers = {'content-type': 'application/json'}
        
        # Send the request to the SoftEther VPN server
        response = requests.request("POST", url=gateway, headers=headers, data=json.dumps(payload), 
                                    verify=True, auth=(username, password))
        data = response.json()
        return data['result']
    except:
        return False

def ser(hubnum):
    """
    Get the status of a single server.
    :param hubnum: The index of the hub in the setup.hub list.
    :return: A string indicating whether the server is online or offline.
    """
    try:
        method = "GetLinkStatus"
        params = {
            "HubName_Ex_str": setup.hub[hubnum][0],
            "AccountName_utf": setup.hub[hubnum][1],
        }
        response = SendCommand(apisite, password, method, params)
        if isinstance(response, dict):
            response = pd.json_normalize(response)['SessionStatus_u32'].values[0]
        if response == 3:
            return f"{setup.hub[hubnum][2]} {msg.server_online}"
        else:
            return f"{setup.hub[hubnum][2]} {msg.server_offline}"
    except:
        return "error"

def all_server():
    """
    Get the status of all servers.
    :return: A string indicating which servers are online and which are offline.
    """
    online_servers = []
    offline_servers = []
    
    try:
        for s in setup.hub:
            method = "GetLinkStatus"
            params = {
                "HubName_Ex_str": s[0],
                "AccountName_utf": s[1],
            }
            response = SendCommand(apisite, password, method, params)
            if isinstance(response, dict):
                response = pd.json_normalize(response)['SessionStatus_u32'].values[0]
            if response == 3:
                online_servers.append(s[2])
            else:
                offline_servers.append(s[2])
                
        if not online_servers:
            online_servers.append(msg.no_online_servers)
        if not offline_servers:
            offline_servers.append(msg.no_offline_servers)
            
        return f"{msg.server_online}\n{online_servers}\n\n{msg.server_offline}\n{offline_servers}"
    
    except:
        return "error"

def client(hubname):
    """
    Get information about clients on a single server.
    :param hubname: The index of the hub in the setup.hub list.
    :return: A string containing information about clients on the specified server.
    """
    
    try:
        method = "EnumUser"
        params = {
            "HubName_str": setup.hub[hubname][0],
        }
        
        response = SendCommand(apisite, password, method, params)
        
        if isinstance(response, dict) and 'UserList' in response:
            response = pd.json_normalize(response['UserList'])[['Name_str', 'Expires_dt', 'Ex.Recv.BroadcastBytes_u64', 'Ex.Send.BroadcastBytes_u64','Ex.Recv.UnicastBytes_u64' ,'Ex.Send.UnicastBytes_u64']].values
            
            for row in response:
                row[0] = f"{msg.before_name} {row[0]}{msg.after_name}"
                row[1] = f"{msg.before_expiry} { msg.no_expiry_message if row[1][:10] == '1970-01-01' else row[1][:10]}{msg.after_expiry}"
                row[2] = f"{msg.before_traffic}{(int(row[2])+int(row[3])+int(row[4])+int(row[5])) // (1048576):,} {msg.after_traffic}"
                row[3] = ""
                row[4] = ""
                row[5] = ""
                
            formatted_response = '\n'.join([''.join(row) for row in response])
            
            return f"{msg.before_server_name} {setup.hub[hubname][2]}{msg.after_server_name}\n{formatted_response}"
        
    except:
        return "error"

def all_client():
    """
    Get information about clients on all servers.
    :return: A string containing information about clients on all servers.
    """
    
    client_name = []
    result = {}
    
    try:
        for s in setup.hub:
            method = "EnumUser"
            params = {
                "HubName_str": s[0],
            }
            
            response = SendCommand(apisite, password, method, params)
            
            if isinstance(response, dict) and 'UserList' in response:
                response = pd.json_normalize(response['UserList'])[['Name_str', 'Expires_dt', 'Ex.Recv.BroadcastBytes_u64', 'Ex.Send.BroadcastBytes_u64','Ex.Recv.UnicastBytes_u64' ,'Ex.Send.UnicastBytes_u64']].values
                
                for user in response:
                    client_name.append(user)
                    
        for c in client_name:
            name, date, value, value2, value3, value4 = c
            if name in result:
                result[name][2] += value
                result[name][3] += value2
                result[name][4] += value3
                result[name][5] += value4 
            else:
                result[name] = [name, date, value, value2, value3, value4]
                
        formatted_response = []
        
        for key in result:
            formatted_response.append(f"{msg.before_name}{result[key][0]}{msg.after_name} {msg.before_expiry}{msg.no_expiry_message if result[key][1][:10] == '1970-01-01' else result[key][1][:10]} {msg.after_expiry}{msg.before_traffic}{(int(result[key][2])+int(result[key][3])+int(result[key][4])+int(result[key][5])) // (1048576):,}{msg.after_traffic}")
            
        return "User list of all servers:" "\n" + '\n'.join(formatted_response)
    
    except:
        return "error"
