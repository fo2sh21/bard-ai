import google.generativeai as genai
import discord
import requests
from PIL import Image
from io import BytesIO

# Create a bot instance
Client = discord.Client(intents=discord.Intents.all())

genai.configure(api_key="AIzaSyD4kkfaLHUl7ZDoRMkigeVCtavZ4Ph_Cvk")
textmodel = genai.GenerativeModel('gemini-pro')
model = genai.GenerativeModel('gemini-pro-vision')
chat = model.start_chat(history=[])
textchat = textmodel.start_chat(history=[])




@Client.event
async def on_ready():
    print(f'Logged in as {Client.user}')

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return

    if message.content:
        if message.attachments:
            for attachment in message.attachments:
                try:
                    image_url = attachment.url
                    image_data = requests.get(image_url).content
                    image = Image.open(BytesIO(image_data))
                    response = chat.send_message(image, stream=True,)
                    response.resolve()
                    await message.channel.send(response.text)
                except Exception as e:
                    print(f"Error processing image: {e}")
        else:
            try:
                response = textchat.send_message(message.content, stream=True)
                response.resolve()
                await message.channel.send(response.text)
            except Exception as e:
                print(f"Error processing text: {e}")

Client.run("MTIwODQzNTUwMTczNzA1NDI4OA.GYJY--.6JrubE0qZNpHad6h4V6c9K1g5oeECzLO4k1UJ4")