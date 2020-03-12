import os

import discord

token = os.getenv('BOT_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!Polo'):
        command = message.content.split()
        if command[1] == "upgrade":
            os.environ["BOT_UPGRADE"] = "yes"
            print(f"Upgrade initiated by {message.author}")
            await client.logout()
        else:
            message.channel.send("?")


async def on_ready():
    print('Logged in as')
    print(client.user.id)
    print('------')

client.run(token)
print("Powering down")
