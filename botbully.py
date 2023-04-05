from twitchio.ext import commands
import super_secret
import nowplayinglogic

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=super_secret.API_KEY, prefix=super_secret.BOT_PREFIX, initial_channels=[super_secret.CHANNEL])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
    
    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        #print everything in chat but self sent messages (cringe) ((don't do this))
        #print(message.content)

        await self.handle_commands(message)

    @commands.command()
    async def np(self, ctx: commands.Context):
        #now playing command for osu
        await ctx.send(f'{nowplayinglogic.getCurrentSong()}')

bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.