import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} giriş yaptı!')

@bot.command()
async def selam(ctx):
    await ctx.send('Selam kanka! Bot çalışıyor 🚀')

@bot.command()
async def tierlist(ctx):
    embed = discord.Embed(title="MC Tierlist Örneği", color=0x00ff00)
    embed.add_field(name="Kullanıcı", value="@kofteekmek", inline=False)
    embed.add_field(name="IGN", value="InuxSamarouS", inline=False)
    embed.add_field(name="Tier", value="LT5", inline=False)
    embed.set_footer(text="MC TierList | Yanlışsa destek aç!")
    await ctx.send(embed=embed)

bot.run(os.getenv('DISCORD_TOKEN'))
