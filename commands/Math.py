from discord.ext import commands
import discord
import asyncio
import random


def setup(bot):
    bot.add_cog(Math(bot))


class Math:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.channel.send(left + right)

    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        """Flips a mothafuckin coin."""
        coin = ["Heads",
                "Tails"]
        await ctx.channel.send(random.choice(coin))

