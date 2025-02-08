# Preface
My current vision for this project is to run deepseekr1 using the 1.5b locally and to somehow have my discord bot capture the input from the user given in chat, run it in ollama, and then capture the output and display it back to the user in the chat. Seems simple enough when typed out and in one sentence, get ollama to run deepseek, have the discord bot provide the input and display the output. I have no idea what I am doing but this will be a learning experience.

# Process
## Setting up ollama
We are going to head over to ollama.com and download based off our OS (I am using the windows download). After it's done downloading, it will install and when it's finished it will open up a command prompt for us. I went ahead and closed it and made a separate directory for it and opened CMD there and typed "ollama -h" and it worked. We now need the model itself, where deepseek comes in. I am going to be using the deepseekR1 1.5B model because I am limited by the technology of my time. The command I will be using is `ollama pull deepseek-r1:1.5b` where pull downloads the model (probably). After it finishes "pulling" the model, you should pray that you see the final word success on your CMD and then you can test if it works by saying `ollama run deepseek-r1:1.5b "What type of an animal is a chinchilla"` and you will be pleasantly suprised to learn that deepseek will inform you that, and I quote, "**Conclusion:** Chinchilla is an adult polar bear.". Oh yeah, its all coming together.

## Testing the API calls
With the model working, we now need to focus on the next section, making sure the API calls works. After some nimble google searching, I was able to deduce that ollama opens a port locally on 14434. After finding that information, I accidently found myself in the documentation of ollama, which is listed in the credits.
















# Credits
- https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion
- https://www.youtube.com/@NetworkChuck
