import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="$", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command(
            aliases=['p'],
            help="This is help",
            description="This is description",
            brief="This is brief",
            enabled=True,
            hidden=False
    )
    async def ping(ctx : commands.Context):
        """ Answers with pong."""
        embed = discord.Embed(colour=discord.Colour.green(), title="PONG")
        await ctx.send(embed=embed)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()