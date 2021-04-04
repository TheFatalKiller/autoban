import discord
from discord.ext import commands

class AutoBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bans = [531602381591543818, 770544017666080770, 543286363156643903, 333808567268147211, 210049870294286337, 812533315222765595, 459476688443801610, 718119648754663475]

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if member.id in self.bans:
            embed = discord.Embed(title="AutoBanned", description="You have been AutoBanned in **Kitty's Paradise**, DM **Fatal#0007** to appeal your removal from banlist.", color=self.bot.main_color)
            await member.send(embed=embed)
            await guild.ban(member, reason="AutoBanned by being placed on the AutoBan List by Fatal")

def setup(bot):
    bot.add_cog(AutoBan(bot))
