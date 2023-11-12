import discord
import traceback
from discord.ext import commands
from .HelpMessageCog import HelpMessageCog
from bot.exceptions import WrongChannelMention, MustBeForum, Gatekept, UnknownTile, TilestratForumNotFound, \
    NotACommunity


class ErrorHandlerCog(HelpMessageCog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__(bot)

    async def cog_app_command_error(self, interaction: discord.Interaction,
                                    error: discord.app_commands.AppCommandError) -> None:
        print("\n\n\n")
        traceback.print_exc()
        print("\n\n\n")

        content = "An error has occurred!"
        thrown_error = error.__cause__
        error_type = type(error.__cause__)
        if error.__cause__ is None:
            error_type = type(error)
            thrown_error = error

        if error_type == WrongChannelMention:
            content = "You did not provide a valid channel! Please *mention* the channel, don't just type its name.\n" + \
                      f"For example, instead of \"{interaction.channel.name}\" it should be \"<#{interaction.channel_id}>\""
        elif error_type == discord.app_commands.errors.MissingPermissions:
            content = "You don't have the perms to execute this command. Sorry!\n" \
                      f"*Needs permissions: {', '.join(thrown_error.missing_permissions)}*"
        elif error_type == discord.app_commands.errors.MissingAnyRole:
            content = "You don't have the perms to execute this command. Sorry!\n" \
                      f"You need to be a manager."
        elif error_type == MustBeForum:
            content = "The channel must be a forum!"
        elif error_type == Gatekept:
            content = "<:hehe:1111026798210326719>"
        elif error_type == UnknownTile:
            content = f"Tile {thrown_error.tile} doesn't exist!"
        elif error_type == discord.errors.Forbidden:
            content = f"I don't have the perms to do that!"
        elif error_type == TilestratForumNotFound:
            content = "You don't have a Tile Strats forum set! " \
                      "Run /tilestratforum create or /tilestratforum set to have one."
        elif error_type == NotACommunity:
            content = "You need to enable Community on your server to run this command!"

        if interaction.response.is_done():
            await interaction.edit_original_response(content=content)
        else:
            await interaction.response.send_message(content, ephemeral=True)
