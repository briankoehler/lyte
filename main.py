import discord
import threading
import server

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

socket_path = '/tmp/lyte.socket'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

def thread_function():
    receiver = server.Server(socket_path)
    receiver.start()

server_thread = threading.Thread(target=thread_function)
server_thread.start()

client.run('TOKEN_HERE')
