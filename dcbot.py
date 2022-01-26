from discord import Client

from load import dp, loop


class MyClient(Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await dp.start_polling()


bot = MyClient(loop=loop)

