import discord
import logging
from datetime import datetime
import bot.db.connection
from bot import __version__
from discord.ext import commands
from config import TOKEN, APP_ID


class CtTicketTracker(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(
            command_prefix=",,,",
            intents=intents,
            application_id=APP_ID,
            activity=discord.Game(name=f"/help"),
            log_level=logging.ERROR,
        )
        self.remove_command("help")
        self.version = __version__
        self.last_restart = datetime.now()
        self.synced_tree = None

    async def setup_hook(self):
        await bot.db.connection.start()
        cogs = [
            "OwnerCog",
            "TrackerCog",
            "LeaderboardCog",
            "TilestratCog",
            "UtilsCog",
            #"VerifyCog",
            "PlannerCog",
            #"WelcomeCog",
            "TilesCog",
        ]
        for cog in cogs:
            await self.load_extension(f"bot.cogs.{cog}")

    async def get_app_command(self, cmd_name: str) -> discord.app_commands.AppCommand or None:
        if self.synced_tree is None:
            self.synced_tree = await self.tree.fetch_commands()
        return discord.utils.get(self.synced_tree, name=cmd_name)

    def reload_version(self):
        with open("bot/__init__.py") as fin:
            for ln in fin:
                ln = ln.strip()
                if ln.startswith("__version__ = \""):
                    self.version = ln[len("__version__ = \""):-1]
                    return


if __name__ == '__main__':
    CtTicketTracker().run(TOKEN)
