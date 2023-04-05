#requried imports
from twitchio.ext import commands

#external scripts to keep main script clean
import super_secret
import nowPlayingLogic

class Bot(commands.Bot):

    def __init__(self):
        #init values from .py script to keep api key private
        super().__init__(token=super_secret.API_KEY, prefix=super_secret.BOT_PREFIX, initial_channels=[super_secret.CHANNEL])

    async def event_ready(self):
        #notify when ready
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
    
    async def event_message(self, message):
        #ignore messages sent by self
        if message.echo:
            return

        #override event_message ignore to allow others to interact
        await self.handle_commands(message)

        #print everything in chat but self sent messages (cringe) ((don't do this))
        #print(message.content)

    @commands.command()
    async def np(self, ctx: commands.Context):
        #now playing command for osu
        await ctx.send(f'{nowPlayingLogic.getCurrentSong()}')

bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.