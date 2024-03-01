import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="$", intents=intents)

    #Event : on_ready
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        for cmd_file in settings.COMMANDES_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"commandes.{cmd_file.name[:-3]}")
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument")

    @bot.command()
    async def load(ctx : commands.context, cog : str):
        await bot.load_extension(f"cogs.{cog.lower()}")

    @bot.command()
    async def reload(ctx : commands.context, cog : str):
        await bot.reload_extension(f"cogs.{cog.lower()}")

    @bot.command()
    async def unload(ctx : commands.context, cog : str):
        await bot.unload_extension(f"cogs.{cog.lower()}")

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()