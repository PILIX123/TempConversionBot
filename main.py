from vault.vault import Vault
from discord import Intents, Client, Message
from commands.commands import reply
from utils.utils import findTempAndDegree
from converters.converter import celciusToFahrenheit, fahrenheitToCelcius

v = Vault()

intents = Intents.none()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

client = Client(intents=intents)


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    values = findTempAndDegree(message)
    if values == None:
        return
    match values[1].lower():
        case 'f':
            return f"{values[0]}°F is {fahrenheitToCelcius(values[0])}°C"
        case 'c':
            return f"{values[0]}°C is {celciusToFahrenheit(values[0])}°F"

client.run(v.get_discord_token())
