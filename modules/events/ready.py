# import discord 
from discord import Status, Activity, ActivityType
from discord.ext import commands, tasks
import random


# create a class instance of a cog.
class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # to keep track of the past activity that is already set.
        self.past_activity = None
        
        # define the activity that will be set.
        self.activities = [f"for {bot.prefix}help", f"for {bot.prefix}info"]
        super().__init__()

    # this is the event that is called when the bot is ready.
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[on_ready] Logged in as {self.bot.user}')

    # create a loop that runs every 5 minutes using tasks.loop that changes the bot's status
    # to predefined statuses.
    @tasks.loop(minutes=5)
    async def change_status(self):
        # remove the activity that was set before.
        removed_activities = self.activities.remove(self.past_activity)
        # get a random activity from the list of activities.
        activity = removed_activities[random.randint(0, len(self.activities) - 1)]
        # set the bot's status to the activity.
        await self.bot.change_presence(
            activity=Activity(
                name=activity,
                type=ActivityType.listening
            )
        )
        # set the past activity to the current activity.
        self.past_activity = activity
        
        # print the activity that is set.
        print(f'[change_status] Set activity to: {activity}')
        
        

