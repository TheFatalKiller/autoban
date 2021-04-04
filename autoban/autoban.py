import discord
from discord.ext import commands

class AutoBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bans = [767398969147392030, 531602381591543818]

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if member.id in self.bans:
            embed = discord.Embed(title="AutoBanned", description="You have been AutoBanned in **{ctx.guild.name}**, DM **Fatal#0007** to appeal your removal from banlist.", color=self.bot.main_color)
            await member.send(embed=embed)
            await guild.ban(member, reason="AutoBanned due to from being placed on the AutoBan List by Fatal")

def setup(bot):
    bot.add_cog(AutoBan(bot))
