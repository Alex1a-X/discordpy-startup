from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def info(ctx):
    await ctx.send('discordで主に活動している キチゲェw 紳士たちの集まりです。')
    
    
@bot.command()
async def infoo(ctx):
    await ctx.send('@everyone[サーバー更新のお知らせ]このサーバーに公式BOTができました！これから機能を追加するのでお待ちください！')

bot.run(token)
