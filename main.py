from vault.vault import Vault
from discord import Intents, Client, Message
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
    listVal = findTempAndDegree(message.content)
    if listVal == None:
        return
    mes = ""
    for values in listVal:
        match values[1].lower():
            case 'f':
                mes += f"{values[0]}°F is {fahrenheitToCelcius(values[0])}°C.\n"
            case 'c':
                mes += f"{values[0]}°C is {celciusToFahrenheit(values[0])}°F.\n"

    await message.reply(mes, mention_author=False)
client.run(v.get_discord_token())
