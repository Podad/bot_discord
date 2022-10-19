import discord
import requests
import discord.ext.commands
import json

intents = discord.Intents().all()
client = discord.Client(intents=intents)

token = "OTIxNDUzNDQ5Mjc3NzYzNTg1.GLJRJe.vunsL7LZ4THiz82wGQ3oEsORWiJrRmnIRhf3W8"

# slash command discord for meme

@client.event
async def on_ready():
    print("Bot is ready")

# noot noot gif command

@client.event
async def on_message(message):
    if message.content.startswith("!noot"):
        print("noot")
        r = requests.get("https://meme-api.herokuapp.com/gimme/nootnoot")
        data = r.json()
        embed = discord.Embed(title=data["title"], color=0x00ff00)
        embed.set_image(url=data["url"])
        await message.channel.send(embed=embed)
    if message.content.startswith("!ping"):
        print("ping")
        await message.channel.send("Pong!")

client.run(token)