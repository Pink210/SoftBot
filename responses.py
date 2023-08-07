import config
import setup

hubs = setup.hub

def get_response(message):
    p_message = message.lower()
    if p_message in [x[3] for x in hubs]:
        index = [x[3] for x in hubs].index(p_message)
        return f'```{config.ser(index)}```'
    elif p_message in [x[4] for x in hubs]:
        index = [x[4] for x in hubs].index(p_message)
        return f'```{config.client(index)}```'
    elif p_message == setup.respon_all_server:
        return f'```{config.ser(0)}\n{config.ser(1)}\n{config.ser(2)}\n{config.ser(3)}\n{config.ser(4)}\n{config.ser(5)}```'
    elif p_message == "hello":
        return f'```{config.client(1)}```'
    elif p_message == "test":
        return "ok"
    return


