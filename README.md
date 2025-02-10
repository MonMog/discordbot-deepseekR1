# Preface
My current vision for this project is to run deepseekr1 using the 1.5b locally and to somehow have my discord bot capture the input from the user given in chat, run it in ollama, and then capture the output and display it back to the user in the chat. Seems simple enough when typed out and in one sentence, get ollama to run deepseek, have the discord bot provide the input and display the output. I have no idea what I am doing but this will be a learning experience.

# Process
## Setting up ollama
We are going to head over to ollama.com and download based off our OS (I am using the windows download). After it's done downloading, it will install and when it's finished it will open up a command prompt for us. I went ahead and closed it and made a separate directory for it and opened CMD there and typed "ollama -h" and it worked. We now need the model itself, where deepseek comes in. I am going to be using the deepseekR1 1.5B model because I am limited by the technology of my time. The command I will be using is `ollama pull deepseek-r1:1.5b` where pull downloads the model (probably). After it finishes "pulling" the model, you should pray that you see the final word success on your CMD and then you can test if it works by saying `ollama run deepseek-r1:1.5b "What type of an animal is a chinchilla"` and you will be pleasantly suprised to learn that deepseek will inform you that, and I quote, "**Conclusion:** Chinchilla is an adult polar bear.". Oh yeah, its all coming together.

## Testing the API calls
With the model working, we now need to focus on the next section, making sure the API calls works. After some nimble google searching, I was able to deduce that ollama opens a port locally on 14434. After finding that information, I accidently found myself in the documentation of ollama (reading will truly take you far), which is listed in the credits. The URL that we need will be `http://localhost:11434/api/generate`. Here is an example of what the API call would look like from their documentation: 

`curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}'`

Like any good programmer, we will take this under our wing and modify it to our heart's content. With that, here is what I used to test (while ollama was running) if the API calls was working

```
import requests

url = "http://localhost:11434/api/generate"
payload = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Do you truly believe that chinchillas are horses?",
    "stream": False
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

The response? Well, here's the first sentence from the response section of the print statement: "The chinchilla is indeed native to Canada and is often mistakenly referred to as a horse by some individuals or communities.". This feeling is similiar to having a baby and taking care of it and you blink and all of a sudden they're leaving the driveway in their own car to college. Can you believe it? The chinchilla is often mistaken as a horse. I think this API call passes with flying colors. 

## Discord bot handling the API request
The final step should be bringing those two first steps together and making the discord bot make the requests themselves. I am going to assume you already have a working discord bot for this step and if not, fret not for there are endless amount of resources online for setting it up yourself. This step should be straight forward, copy the code from the last section to your bot's code, right? Here is what it could look like:

```
import discord
from discord.ext import commands
import requests


Intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=Intents)
token = "niceTry"

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
            "model": "deepseek-r1:1.5b",
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



```


You will notice a helper function inside the code called send_long_message. I have noticed that whenever the model thinks, it _really_ likes to think and goes on and on, which is pretty cool honestly. Because of Discord's message limit of 2000 characters, we will have to find some type of work around. The work around being, cut the reply into chunks of 2000 characters and send them one at a time. I believe we are almost done and we just about to ensure some final steps

## Final steps

Awesome, we have a discord bot that can now call to your locally hosted AI model and input your prompt and output the response to you in the chat. For this to work, you need to ensure that you have ollama running. To check, go to the localhost:port that was previously mentioned and if you see "ollama is running", then your bot can now safely make the calls. I personally want to reduce the amount of steps needed so I made a .bat file that when clicked, just launches CMD and types in the command to run the model

```
@echo off
start cmd /k "ollama run deepseek-r1:1.5b"
```












# Credits
- https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion
- https://www.youtube.com/@NetworkChuck
