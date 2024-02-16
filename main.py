from vault.vault import Vault
from discord import Intents, Client, Message
from utils.utils import findTempAndDegree, findMentionMilage
from converters.converter import celciusToFahrenheit, fahrenheitToCelcius, MPGUSToMPGUK, MPGUKToMPGUS, MPGUSToLPHundredKM, MPGUKToLPHundredKM, LPHundredKMToMPGUS, LPHundredKMToMPGUK

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
    listTemp = findTempAndDegree(message.content)
    listMileage = findMentionMilage(message.content)
    mes = ""
    if listTemp != None:
        for values in listTemp:
            match values[1].lower():
                case 'f':
                    mes += f"{values[0]}°F is {fahrenheitToCelcius(values[0])}°C.\n"
                case 'c':
                    mes += f"{values[0]}°C is {celciusToFahrenheit(values[0])}°F.\n"
        if listMileage == None:
            await message.reply(mes, mention_author=False)
            return
    if listMileage != None:
        for values in listMileage:
            match values[1].lower():
                case 'mpg':
                    mes += f"{values[0]} MPG :flag_us: is {MPGUSToMPGUK(values[0])} MPG :flag_gb:.\n{values[0]} MPG :flag_gb: is {MPGUKToMPGUS(values[0])} MPG :flag_us:.\n{values[0]} MPG :flag_us: is {MPGUSToLPHundredKM(values[0])}L/100KM.\n{values[0]} MPG :flag_gb: is {MPGUKToLPHundredKM(values[0])}L/100KM.\n"
                case _:  # should only trigger with L/100KM
                    mes += f"{values[0]}L/100KM is {LPHundredKMToMPGUS(values[0])} MPG :flag_us:\n{values[0]}L/100KM is {LPHundredKMToMPGUK(values[0])} MPG :flag_gb:"
        await message.reply(mes, mention_author=False)

client.run(v.get_discord_token())
