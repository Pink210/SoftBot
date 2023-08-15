import config
import setup

hubs = setup.hub

def get_response(message):
    # Convert the message to lowercase
    p_message = message.lower()
    
    # Check if the message is in the list of server names
    server_names = [x[3] for x in hubs]
    if p_message in server_names:
        index = server_names.index(p_message)
        return f'```{config.ser(index)}```'
    
    # Check if the message is in the list of client names
    client_names = [x[4] for x in hubs]
    if p_message in client_names:
        index = client_names.index(p_message)
        return f'```{config.client(index)}```'
    
    # Check if the message is the command to respond with all servers
    if p_message == setup.all_server:
        return f'```{config.all_server()}```'
    
    # Check if the message is the command to respond with all client
    if p_message == setup.all_client:
        return f'```{config.all_client()}```'
    
    # Return None if no conditions are met
    return
