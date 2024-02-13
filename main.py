from vault.vault import Vault
from converters.converter import celciusToFahrenheit, fahrenheitToCelcius
from discord import Intents, Client, Message
from utils.utils import findTempAndDegree


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
    values = findTempAndDegree(message.content)
    if values == None:
        return
    match values[1].lower():
        case 'f':
            await message.reply(f"{values[0]}°F is {fahrenheitToCelcius(values[0])}°C", mention_author=False)
            return
        case 'c':
            await message.reply(f"{values[0]}°C is {celciusToFahrenheit(values[0])}°F", mention_author=False)
            return


client.run(v.get_discord_token())
