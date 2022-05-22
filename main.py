from turtle import title
from discord.ext import commands
import discord, nekos, var, config, random, datetime, os, requests

bot = commands.Bot(command_prefix=config.prefix, help_command=None)
TOKEN = config.token

@bot.event
async def on_ready():
    os.system('clear')
    await bot.change_presence(activity=discord.Game(name="with my balls"))
    print(f'\x1b[35m\n Logged in as {bot.user}\n\x1b[0m')


teal = 0x1abc9c


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="All the commands!", color=teal, description="The prefix: >\nCatgirl: Sends a catgirl image\nRoll: Rolls a die\nAvatar: Shows userers avatar\nCat: Sends a cat image\nTroll: Does a lil trolling\nSource: Link to source code")
    await ctx.send(embed=embed)


@bot.command()
async def source(ctx):
    embed=discord.Embed(title="The shit", url="https://github.com/szlug3ns/dumb-bot", description="Source code or smth", colour=teal)
    await ctx.send(embed=embed)

@bot.command()
async def catgirl(ctx):
    embed=discord.Embed(title="Catgirl", url="https://nekos.life/", description="Cool", color=teal)
    embed.set_image(url=(nekos.img('neko')))
    await ctx.send(embed=embed)

@bot.command()
async def roll(ctx):
    embed = discord.Embed(title=":game_die: Roll the die.", color=teal)
    embed.add_field(name=ctx.message.author.name + "'s, roll:", value="{}".format(random.randint(var.minimum, var.maximum)), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx):
    embed = discord.Embed(color=teal, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=ctx.author.name, url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
    embed.set_image(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def cat(ctx):
    embed=discord.Embed(title="Cat", url="https://nekos.life/", description="Cute cat too", color=teal)
    embed.set_image(url=(nekos.cat()))
    await ctx.send(embed=embed)

        
@bot.command()
async def troll(ctx, member:discord.Member=None):
    if member is None:
        embed=discord.Embed(title="Troll", url="https://api.nekos.cc/troll", description=f'{ctx.author.name} wants to do a little trolling', color=teal)
        embed.set_image(url=('https://api.nekos.cc/troll'))
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Troll", url="https://api.nekos.cc/troll", description=f'{ctx.author.name} trolls {member.name} :trolley:', color=teal)
        embed.set_image(url=('https://api.nekos.cc/troll'))
        await ctx.send(embed=embed)

bot.run(TOKEN)
