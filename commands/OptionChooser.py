from discord.ext import commands
import discord
import asyncio
import random


def setup(bot):
    bot.add_cog(OptionChooser(bot))


class OptionChooser:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def choose(self, ctx, *option1):
        """chooses an option"""
        await ctx.channel.send(random.choice(option1))
