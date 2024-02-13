from vault.vault import Vault
from discord import Intents, Client, Message
from commands.commands import reply

v = Vault()

intents = Intents.none()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

client = Client(intents=intents)


@client.event
async def on_message(message: Message):
    await message.reply(reply(message, client.user), mention_author=False)

client.run(v.get_discord_token())
