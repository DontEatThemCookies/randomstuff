import discord # discord.py dependency

class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot ready.', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!command':
            await message.channel.send('Command executed.')

client = MyClient()
client.run('Insert Discord Bot Token Here')
