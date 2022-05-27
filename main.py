from turtle import title
from discord.ext import commands
import discord, nekos, var, config, random, datetime, os, requests

bot = commands.Bot(command_prefix=config.prefix, help_command=None)
TOKEN = config.token

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="women being stupid"))
    print(f'\x1b[35m\n Logged in as {bot.user}\n\x1b[0m')

teal = 0x1abc9c
trollface = var.trollface

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="All the commands!", color=teal, description="The prefix: >\nCatgirl: Sends a catgirl image\nRoll: Rolls a die\nAvatar: Shows userers avatar\nCat: Sends a cat image\nTroll: Does a lil trolling\nBan: Bans a user\nUnban: Unbans a user\nSource: Link to source code")
    await ctx.send(embed=embed)

@bot.command()
async def source(ctx):
    embed=discord.Embed(title="The shit", url="https://github.com/szlug3ns/dumb-bot", description="Source code or smth", colour=teal)
    await ctx.send(embed=embed)

@bot.command()
async def catgirl(ctx):
    embed=discord.Embed(title="Catgirl", description="Cool", color=teal)
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
    embed=discord.Embed(title="Cat", description="Cute cat too", color=teal)
    embed.set_image(url=(nekos.cat()))
    await ctx.send(embed=embed)

        
@bot.command()
async def troll(ctx, member:discord.Member=None):
    if member is None:
        embed=discord.Embed(title="Troll", description=f'{ctx.author.name} does a little trolling', color=teal)
        embed.set_image(url=trollface)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Troll", description=f'{ctx.author.name} trolls {member.name}', color=teal)
        embed.set_image(url=trollface)
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



bot.run(TOKEN)
