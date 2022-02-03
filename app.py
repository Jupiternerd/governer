# imports
import discord
from discord.ext import commands
import os
from os import listdir
from os.path import isdir, isfile, join
# extend discord.Client class to create bot
class Governer(commands.bot):
    def __init__(self):
        # get token from environment variable
        self.token = os.environ.get('TOKEN')
        
        # declare intents
        intent = discord.Intents.default()
        intent.members = True;
        
        super().__init__(command_prefix='+', intents=intent)
        
    def login(self):
        # login to discord
        self.remove_command('help')
        self.run(self.token);
        
    def load_modules(self, path = './modules'):
         for filename in listdir(path):
            file = join(path, filename) # get full path of the file
            if not filename.startswith("__"):
                
                # if the file is actually a file and not a directory
                if isfile(file):
                    
                    # if the file is a .py file
                    if filename.endswith('.py'):
                        cogPath = path[2:].replace("\\", ".") # remove ./ from path
                        self.load_extension(f'{cogPath}.{filename[:-3]}') # load the module
                        print(f"[load_cogs] Loaded Cog [ {filename} ]")
                        
                if isdir(file):
                    
                    # if the path is a directory then rerun this function but with this file directory to search in.
                    self.load_cogs(file)
        
        
    
    
        
