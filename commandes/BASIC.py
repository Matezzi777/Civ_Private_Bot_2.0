import discord
from discord.ext import commands        

@commands.group()
async def BASIC(ctx : commands.Context):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to BASIC.")

@BASIC.command(
            aliases=['p'],
            help="Respond '🟢 Pong !' if the client is live.",
            description="BASIC",
            brief="- Respond PONG",
            enabled=True,
            hidden=False
)
async def ping(ctx : commands.Context):
    await ctx.send("🟢 Pong !")

@BASIC.command(
            aliases=['s'],
            help="Repeat the the string passed in argument.",
            description="BASIC",
            brief="- Repeat something",
            enabled=True,
            hidden=False)
@commands.is_owner()
async def say(ctx : commands.Context, *content : str):
        await ctx.send(" ".join(content))

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Permission denied")
        

@BASIC.command(
            help="Gives some informations about an user (his name & when he joined)",
            description="BASIC",
            brief="- Basic info about the user",
            enabled=True,
            hidden=False)
async def joined(ctx : commands.Context, user : discord.Member):
        await ctx.send(f"**User** : {user}\nJoined at : {user.joined_at}")

async def setup(bot):
      bot.add_command(BASIC)
      bot.add_command(ping)
      bot.add_command(say)
      bot.add_command(joined)