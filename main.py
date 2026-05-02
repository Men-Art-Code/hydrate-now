import time
import discord
from discord import opus
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def notification(vc, duration):
    if duration is not None:
        time.sleep(int(duration))
    else:
        time.sleep(1200)

    if not vc.is_playing():
        vc.play(discord.FFmpegPCMAudio('Water.mp3'), after=lambda x: notification(vc, duration))

@bot.command()
async def join(ctx, duration=None):
    if (ctx.author.voice):
        # Access the command author's voice channel
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        notification(vc, duration)

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.event
async def on_voice_state_update(member, before, after):
    channelStatus = member.guild.voice_client
    # Check if the bot is connected and alone
    if channelStatus is not None and len(channelStatus.channel.members) < 2:
        await channelStatus.disconnect()

bot.run('TOKEN')
