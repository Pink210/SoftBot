import requests
import json
import setup
import pandas as pd

server = setup.server_pass[0]
apisite = f"https://{server}:5555/api/"
password = setup.server_pass[1]

username = ""

def SendCommand(gateway,password,method,params):
	try:
		payload = {
      	"jsonrpc": "2.0",
	        "id": "rpc_call_id",
        	"method": method,
          "params": params
    	}
		headers= {'content-type': 'application/json'}
		response = requests.request("POST", url=gateway, headers=headers, data = json.dumps(payload), 
			verify = False, auth = (username,password))
		data = response.json()
		return data['result']
	except:
		return False

def ser(hubnum):
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
                return f"{setup.hub[hubnum][2]} Online"
    except:
        return f"{setup.hub[hubnum][2]} Offline"

def client(hubname):
    try:
        method = "EnumUser"
        params = {
            "HubName_str": setup.hub[hubname][0],
        }
        response = SendCommand(apisite, password, method, params)
        if isinstance(response, dict) and 'UserList' in response:
            response = pd.json_normalize(response['UserList'])[['Name_str', 'Expires_dt', 'Ex.Recv.BroadcastBytes_u64']].values
            for row in response:
                row[0] = f"{row[0]} |"
                row[1] = f"Ex date: {'No Ex' if row[1][:10] == '1970-01-01' else row[1][:10]} |"
                row[2] = f"Traffic: {row[2] // (1024):,} MB"
            formatted_response = '\n'.join([' '.join(row) for row in response])
            return f"User list of {setup.hub[hubname][2]} \n {formatted_response} Server"
    except:
        return "error"