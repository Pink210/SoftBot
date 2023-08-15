# Import the time module to keep track of time.
import time

# Import the Discord module and the task's extension to interact with the Discord API.
import discord
from discord.ext import tasks

# Import the config, responses, and set-up modules from local files.
import config
import responses
import setup
import msg


# Import variables from the config module for convenience
all_client = config.all_client()
all_server = config.all_server()
TIMER = int(setup.timer)
COOLDOWN = int(setup.cooldown)

# Set the cooldown time in seconds (120 seconds = 2 minutes).
COOLDOWN_TIME = COOLDOWN
# Initialize a variable to keep track of the last time the bot sent a message.
last_message_time = 0

async def send_message(message, user_message, is_private):
    """
    Sends a response to the user's message.

    :param message: The message object from the Discord API.
    :param user_message: The content of the user's message.
    :param is_private: A boolean indicating whether the response should be sent as a private message or not.
    :return: None
    """
    global last_message_time
    # Get the current time in seconds since the epoch.
    current_time = time.time()
    # Check if enough time has passed since the last message was sent.
    if current_time - last_message_time >= COOLDOWN_TIME:
        try:
            # Get a response to the user's message using the responses module.
            response = responses.get_response(user_message)
            # Send the response as a private message or in the channel, depending on the value of is_private.
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
            # Update the last message time to the current time.
            last_message_time = current_time
        except Exception as e:
            print(e)
    else:
        return f"```{msg.cooldown_message}```"



def run_discord_bot():
    """
    This function sets up and runs the Discord bot by creating a new Discord client object,
    setting up event handlers, and starting the bot using the specified token.
    """
    # Get the bot token from the setup module.
    TOKEN = setup.token
    # Set up the intents for the bot.
    intents = discord.Intents.default()
    intents.message_content = True
    # Create a new Discord client object with the specified intents.
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        """
        This function is called when the bot is ready and connected to Discord.
        """
        print(f"Bot is now running")
        send_hello_world.start()

    @tasks.loop(hours=TIMER)
    async def send_hello_world():
        channel = discord.utils.get([c for c in client.get_all_channels() if isinstance(c, discord.TextChannel)], name=setup.channel_name)
        if channel:
            await channel.send(f'```{all_client}```')
            await channel.send(f'```{all_server}```')

    send_hello_world.before_loop(client.wait_until_ready)
    
    @client.event
    async def on_message(message):
        """
        This function is called when a new message is received by the bot.
        :param message: The message object from the Discord API.
        """
        # Ignore messages sent by the bot itself.
        if message.author == client.user:
            return

        # Extract information from the message object.
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #For debug porpess
        #print(f'{username} said:"{user_message}" ({channel})')

        # Check if the message was sent in the specified channel or not.
        if channel == setup.channel_name:
            response = await send_message(message, user_message, is_private=False)
            if response:
                await message.channel.send(response)
        else:
            response = await send_message(message, user_message, is_private=True)
            if response:
                await message.author.send(response)

    # Run the bot using the specified token.
    client.run(TOKEN)
