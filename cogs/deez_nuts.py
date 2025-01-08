import discord, socket, asyncio
from discord import app_commands
from discord.ext import commands


class Deez_Nuts(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="avatar", description="Gets a user's avatar")
    async def av(self, intr, user: discord.User = None):
        if user is None:
            user = intr.user

        await intr.response.send_message(user.display_avatar)

    @app_commands.command(name="sathya", description="Sathya Sathya'd Sathya")
    async def sathya(self, intr, member: discord.Member):
        if intr.user.id != 444895960577998860:
            await intr.response.send_message("You aren't Sathya! \>:(", ephemeral=False)
            return
        else:
            try:
                await member.edit(nick="Sathya")
                await intr.response.send_message(f"{intr.user.mention} Sathya'd {member.mention}", ephemeral=False)
                return
            except:
                await intr.response.send_message(f"I could not change this user's nickname. :pensive:", ephemeral=False)

    @app_commands.command(name="yeet", description="By community vote, silence your classmates!")
    async def yeet(self, intr, member: discord.Member):
        print()

    @app_commands.command(name="modabuse", description="Mod abuse")
    async def modabuse(self, intr, member: discord.Member):
        print()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Deez_Nuts(bot))