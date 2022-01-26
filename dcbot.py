from discord import Client

from load import dp, loop


class MyClient(Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        me = await dp.bot.get_me()
        print("{first_name} [@{username}]"
            .format(first_name=me.first_name, username=me.username)
        )
        await dp.start_polling()


bot = MyClient(loop=loop)

