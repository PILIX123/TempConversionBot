from vault.vault import Vault
from discord import Intents, Client, Message
from utils.utils import findTempAndDegree, findMentionMilage, findMentionLength
from converters.converter import celciusToFahrenheit, fahrenheitToCelcius, MPGUSToMPGUK, \
    MPGUKToMPGUS, MPGUSToLPHundredKM, MPGUKToLPHundredKM, LPHundredKMToMPGUS, LPHundredKMToMPGUK, \
    milesToKM, yardToM, footToCM, inchToCM, KMToMiles, MToYard, CMToFoot, CMToInch
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
    listLength = findMentionLength(message.content)
    mes = ""
    if listTemp != None:
        for values in listTemp:
            match values[1].lower():
                case 'f':
                    mes += f"{values[0]}°F is {fahrenheitToCelcius(values[0])}°C.\n"
                case 'c':
                    mes += f"{values[0]}°C is {celciusToFahrenheit(values[0])}°F.\n"
    if listMileage != None:
        for values in listMileage:
            match values[1].lower():
                case 'mpg':
                    mes += f"{values[0]} MPG :flag_us: is {MPGUSToMPGUK(values[0])} MPG :flag_gb:.\n{values[0]} MPG :flag_gb: is {MPGUKToMPGUS(values[0])} MPG :flag_us:.\n{values[0]} MPG :flag_us: is {MPGUSToLPHundredKM(values[0])}L/100KM.\n{values[0]} MPG :flag_gb: is {MPGUKToLPHundredKM(values[0])}L/100KM.\n"
                case _:  # should only trigger with L/100KM
                    mes += f"{values[0]}L/100KM is {LPHundredKMToMPGUS(values[0])} MPG :flag_us:\n{values[0]}L/100KM is {LPHundredKMToMPGUK(values[0])} MPG :flag_gb:"
    if listLength != None:
        for values in listLength:
            if values[1].lower() in ["miles", "mi", "mile"]:
                mes += f"{values[0]} miles is {milesToKM(values[0])} KM.\n"
            elif values[1].lower() in ["yards", "yard", "yd", "yds"]:
                mes += f"{values[0]} yard(s) is {yardToM(values[0])} m.\n"
            elif values[1].lower() in ["ft", "foot", "feet"]:
                v = footToCM(values[0])
                if v > 100:
                    mes += f"{values[0]} foot/feet is {round(v/100,2)} m.\n"
                else:
                    mes += f"{values[0]} foot/feet is {v} cm.\n"
            elif values[1].lower() in ["in", "inches", "inch"]:
                mes += f"{values[0]} inch(es) is {inchToCM(values[0])} cm.\n"
            elif values[1].lower() in ["km", "kms", "kilo", "kilos", "kilometer", "kilometers"]:
                mes += f"{values[0]} KM is {KMToMiles(values[0])} mi.\n"
            elif values[1].lower() in ["meter", "meters", "m"]:
                mes += f"{values[0]} M is {MToYard(values[0])} yd(s).\n"
            elif values[1].lower() in ["cm", "cms", "centimeter", "centimeters"]:
                v = CMToInch(values[0])
                if (v > 12):
                    mes += f"{values[0]} CM is {CMToFoot(values[0])} ft.\n"
                else:
                    mes += f"{values[0]} CM is {CMToInch(values[0])} in.\n"
    if mes != "":
        await message.reply(mes, mention_author=False)

client.run(v.get_discord_token())
