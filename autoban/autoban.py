import discord
from discord.ext import commands

class AutoBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bans = [728408480251117654, 529439074013020168, 804861326244708373, 197137836518932480, 613249974163210261, 613137906646646807, 399733547281285121, 716312920362975252, 491610326496837642, 755547592842149950, 531602381591543818, 543286363156643903, 333808567268147211, 210049870294286337, 812533315222765595, 459476688443801610, 718119648754663475]

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        channel = self.bot.get_channel(834839320115675230)
        if member.id in self.bans:
            embed = discord.Embed(title="AutoBanned", description=f"You have been AutoBanned in **{guild.name}**, DM **Fatal#7702** to appeal your removal from banlist, or appeal your ban by visiting this forum: https://forms.gle/ty29zXraHfxHQpkx6", color=self.bot.main_color)
            em = discord.Embed(title="Autoban Logs", description=f"{member} was autobanned")
            await member.send(embed=embed)
            await channel.send("<@199622722660204545>")
            await channel.send(embed=em)
            await guild.ban(member, reason="AutoBanned by being placed on the AutoBan List by Fatal")
def setup(bot):
    bot.add_cog(AutoBan(bot))
