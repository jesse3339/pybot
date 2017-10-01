from discord.ext import commands
import discord
import asyncio
import random


def setup(bot):
    bot.add_cog(ChooseLocation(bot))


class ChooseLocation:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pubg(self, ctx):
        """Lists a random location in PUBG when you can't fucking decide for yourself."""

        locations = ["Zharki",
                     "School",
                     "Novo",
                     "Pochinki",
                     "Gatka",
                     "Mylta",
                     "Military Base",
                     "Military Base",
                     "Military Base",
                     "Military Base",
                     "Military Base",
                     "Military Base",
                     "Military Base",
                     "Georgepol Apps",
                     "Georgepol Crates",
                     "Yasmaya",
                     "Kamenshki",
                     "RozCOCK",
                     "Primorsk",
                     "Hospital",
                     "Severny",
                     "Bunkers",
                     "Mylta Power",
                     "BRIDGE CAMP",
                     "Lipovka"]
        string = input().
        await ctx.channel.send(random.choice(locations))

    @commands.command(pass_context=True)
    async def pubglist(self, ctx):
        """Lists a random location in PUBG when you can't fucking decide for yourself."""

        locations = ["Zharki",
                     "School",
                     "Novo",
                     "Pochinki",
                     "Gatka",
                     "Mylta",
                     "Military Base",
                     "Georgepol Apps",
                     "Georgepol Crates",
                     "Yasmaya",
                     "Kamenshki",
                     "RozCOCK",
                     "Primorsk",
                     "Hospital",
                     "Severny",
                     "Bunkers",
                     "Mylta Power",
                     "BRIDGE CAMP",
                     "Lipovka"]
        msg = ""

        for x in locations:
            msg = msg + x + ", "

        await ctx.channel.send(msg)

    @commands.command(pass_context=True)
    async def fn(self, ctx):
        """Lists a random location in Fortnite when you can't fucking decide for yourself."""

        locations = ["Pleasant Park",
                     "Greasy Grove",
                     "Loot Lake",
                     "Anarchy Acres",
                     "Wailing Woods",
                     "Lonely Lodge",
                     "Retail Row",
                     "Fatal Fields",
                     "Moisty Mire",
                     "Flush Factory",
                     "Those houses in the middle"]

        await ctx.channel.send(random.choice(locations))
