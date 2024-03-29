from json.decoder import JSONDecodeError
from discord.ext import commands
import discord


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = "Oh no! Something went wrong while running the command!"
            print(error)

        embed = discord.Embed(title="Error!", description=f"{message}", colour=discord.Colour.random())
        await ctx.send(embed=embed, delete_after=5)

async def setup(bot: commands.Bot):
    await bot.add_cog(ErrorHandler(bot))