from datetime import datetime
import discord
from pull import Pull
from discord.ext import commands
import asyncio 
from itertools import cycle
import json
from token import Token
import simplejson


data = Pull()
token = Token()





intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)    




async def write_file():
    while not client.is_closed():

        rows = data.return_data()
        #client.get_all_members()
        

        for r in rows:
            for c in client.get_all_members():
                if c.nick is None:
                    disc_nickname = c.name
                
                else:
                    disc_nickname = c.nick
                
                row_nickname = r[0]
                row_id= r[1]
                
                disc_id = c.name

                

                if row_nickname in disc_nickname and row_id==disc_id:
                    
                    rows.remove(r)
                    
                    

        currtime = datetime.now()    
        conflicts = [[str(currtime.strftime("%m/%d/%Y, %H:%M:%S"))], [rows]]

        with open('conflicts.txt', 'w') as outfile:
            simplejson.dump(conflicts, outfile)
        
        

       
        
        await asyncio.sleep(10)



@client.event    
async def on_ready():
    print('Logged on!')

    

@client.command()
async def conflicts(ctx):
    
    if ctx.author.name == "sdhjfgsdjfghdjk" or ctx.author.nick== "jfgljdfl" or ctx.author.name== "gdfhjdjfghdf" or ctx.author.nick == "sjdhsfkd" or ctx.author.name == "djkfhsdfkhsdf"or ctx.author.name == "dsjflsdfkjsfd":
        
        channel = await ctx.author.create_dm()
        await channel.send(file=discord.File('./conflicts.txt'))
        


client.loop.create_task(write_file())
client.run(token.return_token)




