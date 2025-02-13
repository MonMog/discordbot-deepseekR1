import discord
from discord.ext import commands
import requests


Intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=Intents)
token = "--->YOURTOKENHERE!!!!<---"

OLLAMA_API_URL = "http://localhost:11434/api/generate"

async def send_long_message(channel, message):
    for i in range(0, len(message), 2000):
        await channel.send(message[i:i + 2000])

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[5:].strip()
        if not prompt:
            await message.channel.send("You sicken me")
            return

        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            reply = data.get("response", "Hmmmmmmmmm")
        else:
            reply = f"Error: {response.status_code}"

        if len(reply) > 2000:
            await send_long_message(message.channel, reply)
        else:
            await message.channel.send(reply)


bot.run(token)


