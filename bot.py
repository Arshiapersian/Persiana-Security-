from discord.ext import commands
import discord
from discord.ext import commands
import time
from asyncio import sleep
from discord.ext import tasks
from discord import Embed, Member
from datetime import datetime, timedelta
import random
import requests
import urllib
from colorama import Fore
import urllib.request
import config
import datetime
import aiohttp
import youtube_dl
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
from discord import File
from PIL import Image, ImageDraw, ImageFont
import io
from discord.utils import find
import asyncio
import string
import youtube_dl



bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Executing System...")
    time.sleep(2)
    print("Starting System...")
    time.sleep(3)
    print("Excuting Status...")
    change_status.start()
    while True:
        await asyncio.sleep(13)
        with open("arshiapersiana.txt", "r+") as file:
            file.truncate(0)  



@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title="<a:system:848585859459973152> Persiana",
    color=0x4146d1)
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f" <a:nop:859487904694009877>شما دسترسی ندارید {ctx.author.mention}")
    else:
        return
        #embed.add_field(name = f'<a:nop:859487904694009877>  یکی پاش رفته روی سیم ', value = f"{error}")
        #await ctx.send(embed = embed)   

for ext in ('fun', 'levelling'):
    bot.load_extension(f'cogs.{ext}')
# security
#--------------------------------------------------------------------------------------------------
Servers = {841340667041021972}
badword_Eng = ['fuck', 'porn', 'hentai', 'kir', 'boobs', 'anal', 'koni', 'kooni', 'koon', 'jende', 'suck', 'sic', 'xnxx', 'xxx', 'madaret', 'k o s', 'goshad', 'sex', 'jagh', 'tokh', 'mali', '🖕', 'nanat', 'dil', 'dick', 'Fountai', 'pussy', 'kos']
badword_ir = ['بی ناموس', 'حروم', 'دیل ', 'کص', 'بخورش', 'تخم', 'مال', 'جغ', 'بگا', 'جق ', 'گای', ' میگا', ' خایه', 'سکس', 'سیک', 'شاشو', 'جند', 'کیر', ' کوص', ' کون', 'شاش', 'ننت', 'خار', ' کردمت', 'مادرتو کردم', 'میکنمت', 'کسکش', 'کس کش', 'کص کش', 'کصکش', 'کوص', 'کون', 'گای']
selfbot = ['massmention', 'masskick', 'massban', 'massdel', 'nuck', 'btc', 'eth']
GlobalBanned = {}
#----
# Persiana Community = 841340667041021972 
# Persiana Update = 859085218979774495
#-------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    counter = 0
    with open("arshiapersiana.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1

        file.writelines(f"{str(message.author.id)}\n")
        if counter > 9:
            if message.guild.id in Servers:
                await message.channel.edit(slowmode_delay=10) 
                await message.channel.send("انتی اسپم فعال شد <a:Ver:847030966614753301>")
                await asyncio.sleep(60)
                await message.channel.edit(slowmode_delay=5) 

    if message.guild.id in Servers:
        for i in badword_Eng:
            if i in message.content:
                await message.delete()
                embed=discord.Embed(title=f"<a:Global:853191421431644171> Banned word \n Username: {message.author} \n ID: {message.author.id}\n reason : English banned words", color= 0x3498db)
                embed.set_image(url=message.author.avatar_url)
                embed.set_footer(text="Persiana security team")
                channel = bot.get_channel(885797326541688843)
                await channel.send(embed=embed) 
                bot.dispatch('profanity', message, i)
                return 
    if message.guild.id in Servers:  
        for i in badword_ir:
            if i in message.content:
                await message.delete()
               
                embed=discord.Embed(title=f"<a:Global:853191421431644171> Banned word \n Username: {message.author} \n ID: {message.author.id}\n reason : iranian banned words", color= 0x3498db)
                embed.set_image(url=message.author.avatar_url)
                embed.set_footer(text="Persiana security team")
                channel = bot.get_channel(885797326541688843)
                await channel.send(embed=embed) 
                bot.dispatch('profanity', message, i)
                return 

    if message.guild.id in Servers:      
        for i in selfbot:
            if i in message.content:
                await message.delete()
                embed=discord.Embed(title=f"<a:Global:853191421431644171> Banned selfbot Commands \n Username: {message.author} \n ID: {message.author.id}\n reason : used selfbot commands ", color= 0x3498db)
                embed.set_image(url=message.author.avatar_url)
                embed.set_footer(text="Persiana security team")
                channel = bot.get_channel(885797326541688843)
                await channel.send(embed=embed) 
                bot.dispatch('profanity', message, i)
                return  

    if message.author.id in GlobalBanned:
        if message.guild.id in Servers:
            await message.author.ban(reason="این شخص از طرف تیم امنیتی در لیست سیاه قرار داده شد!")
            embed=discord.Embed(title=f"اسم: {message.author}\nایدی: {message.author.id}\n این شخص در لیست سیاه هست و به دلیل وارد شدن به سرور تحت امنیت پرشیانا بن شد از !\n-----------\n This User Is Banned From Persiana And when This User Tried To join Protected Server by Persiana was Banned.", color= 0x3498db)
            embed.set_image(url=message.author.avatar_url)
            embed.set_footer(text="Persiana Security")
            channel = bot.get_channel(885797326541688843) 
            await channel.send(embed=embed) 


    await bot.process_commands(message)       


@bot.event
async def on_member_join(member):
    if member.id in GlobalBanned:
        if member.guild.id in Servers:
            await member.ban(reason="Persiana Security. Global Banned")
            embed=discord.Embed(title="**<:PersianaSecurity:848953177867812875> Global Protection**", description=f"\n Global banned\n user: {member}\n User ID: {member.id}\n reason: This User was Trying To join protected server by persiana Bot.\n Status:Banned.", color= RandomColor())
            channel = bot.get_channel(885797326541688843) 
            await channel.send(embed=embed) 
            await member.ban(reason="Persiana Security. Global Banned")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@tasks.loop(seconds=60)
async def change_status():
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Game(name="❤️Persiana Team"))
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Game(name="❓Do You have problem Use : !help"))
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Game(name="💚Join Our Discord"))
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Game(name="🌐 Live The moment now"))
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Game(name="💙Persiana Community"))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#commands admin
@bot.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"{seconds} ")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
      await ctx.channel.purge(limit=amount)
      embed=discord.Embed(title="Cleared Chat", description="massege has been cleared", color=discord.Color.blue())
      await ctx.send(embed=embed)

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    embed=discord.Embed(title="muted", description=f"muted {member.mention} for reason {reason}.", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

    await member.remove_roles(mutedRole)
    embed=discord.Embed(title="Unmuted", description=f"Unmuted {member.mention}", color=discord.Color.blue())
    await ctx.send(embed=embed)  

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed=discord.Embed(title="Banned", description=f"{member} was Banned From Server -", color=discord.Color.blue())
    await ctx.send(embed=embed)  

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed=discord.Embed(title="kicked", description=f"{member} was kicked From Server -", color=discord.Color.blue())
    await ctx.send(embed=embed)  

@bot.command()
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + "Has been lockdown")

@bot.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send( ctx.channel.mention + "Has been unlocked")

@bot.command()
@commands.has_permissions(manage_channels = True)
async def setantifile(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, attach_files=False)
    await ctx.send( ctx.channel.mention + "Anti File Is Active-")

@bot.command()
@commands.has_permissions(manage_channels = True)
async def removeantifile(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, attach_files=True)
    await ctx.send( ctx.channel.mention + "Anti File Is deactive-")

@bot.command()
async def massunban(ctx):
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await ctx.guild.unban(user=users.user)
        except:
            pass
    await ctx.send("Unbaning All banned members.")       

#---------------------------------------------------------------------------------------
#--helps
@bot.command()
@commands.has_permissions(manage_messages=True)
async def moderation(ctx, category=None):
    if category is None:
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="<a:herp:859494461255974972> سلام ادمین و هلپر و تمام دست اندرکاران", value="<a:herp2:859505382841516052> سلام به همگی دوستان. ما با تلاش چند ماهه تلاش کردیم تمام نیاز های شما دوستان را برای مدیریت صحیح سرور فراهم کنیم امیدوارم به موفقید های بزرگی برسبد", inline=False)
        embed.add_field(name="`!kick [شخص]`", value="<:kick:859808070347653151> .جهت کیک کردن شخص از سرور  ", inline=True)
        embed.add_field(name="`!ban [شخص]`", value="<a:ban:859809002388455424> .جهت بن زدن شخص از سرور", inline=True)
        embed.add_field(name="`!mute [شخص]`", value="<a:nop:859487904694009877> .جهت میوت کردن شخص از سرور با این دستور شخص قادر به ارسال پیام نمی باشد", inline=False)
        embed.add_field(name="`!unmute [شخص]`", value="<a:yes:859493855410126868> .جهت ان میوت کردن شخص از سرور", inline=True)
        embed.add_field(name="<a:system:848585859459973152> .جهت مدیریت خود سرور و چنل ها از این دستورات زیر استفاده کنید", value="<a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100>", inline=False)
        embed.add_field(name="`!slowmode [زمان]`", value="<a:loading:859812870275334164>. با این دستور می توانید زمان ارسال پیام برای اعضا تایین کنید و پیشنهادد ما 5 ثانیه هست", inline=False)
        embed.add_field(name="`!lockdown `", value="<a:locking:859814116410523719> جهت قفل کردن چنل و اعضا دیگر قادر به ارسال پیام در ان چنل نیستند.", inline=True)
        embed.add_field(name="`!unlock `", value="<a:locking:859814116410523719> جهت باز کردن چنل از حالت قفل", inline=True)
        embed.add_field(name="`!setantifile `", value=":file_folder:جهت ممنوع کردن ارسال فایل در چنل", inline=False) 
        embed.add_field(name="`!removeantifile `", value=":file_folder:جهت باز کردن ارسال فایل در چنل", inline=True)  
        embed.add_field(name="`!massunban `", value=":file_cabinet: جهت انبن کردن همه ی اعضای بن شده", inline=False) 
        embed.add_field(name="`!clear `", value="<a:Ver:847030966614753301> جهت پاک کردن پیام های ارسال شده", inline=True) 
        embed.add_field(name="<a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100>", value="<a:Global:853191421431644171>جهت دیدن امنیت سرور خود از دستور `seurtiy!` استفاده کنید", inline=False)
        embed.set_footer(text="Persiana Team")
        await ctx.send(embed=embed)

@bot.command()
async def security(ctx, category=None):
    if ctx.guild.id in Servers:  
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="**<a:system:848585859459973152> Server Protection**                                    premium server: <:active:859823173968986112>", value="امنیت شما به صورت زیر است و در صورت نیاز به سرور پشتیانی استفاده کنید<a:Ver:847030966614753301>", inline=False)
        embed.add_field(name="<a:Global:853191421431644171> Global Protection", value="...جلوگیری از ورود اشخاص ممنوعه به سرور شما مانند افشاگران و دزدان و  \n وضعیت: <:active:859823173968986112>", inline=True)
        embed.add_field(name="<a:locking:859814116410523719> Anti spam chat", value="   جلوگیری از اسپم دادن در چت و جلوگیری از ان \n وضعیت: <:active:859823173968986112>", inline=True)
        embed.add_field(name="<a:system:859814116410523719> Banned word Ennglish", value="جلوگیری از فرستادن فحش های انگیلیسی و لاتین ایرانی\n وضعیت: <:active:859823173968986112>", inline=False)
        embed.add_field(name="<a:system:848585859459973152> Banned word Irani", value="جلوگیری از فرستادن فحش های ایرانی\n وضعیت: <:active:859823173968986112>", inline=False)
        embed.add_field(name="<a:locking:859814116410523719> Banned Link", value="جلوگیری از فرستادن لینک های بد به سرور\n وضعیت: <:active:859823173968986112>", inline=False)
        embed.add_field(name="<a:locking:859814116410523719> Anti raid,nuck", value="جلوگیری از حملات به سرور\n وضعیت: <:active:859823173968986112>", inline=False)
        embed.set_footer(text="Persiana Team")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="**<a:system:848585859459973152> Server Protection**                                      premium server: <:deactive:859861439929253899>", value="امنیت شما به صورت زیر است و در صورت نیاز به سرور پشتیانی استفاده کنید<a:Ver:847030966614753301>", inline=False)
        embed.add_field(name="<a:Global:853191421431644171> Global Protection", value="...جلوگیری از ورود اشخاص ممنوعه به سرور شما مانند افشاگران و دزدان و  \n وضعیت: <:deactive:859861439929253899>", inline=True)
        embed.add_field(name="<a:locking:859814116410523719> Anti spam chat", value="   جلوگیری از اسپم دادن در چت و جلوگیری از ان \n وضعیت: <:deactive:859861439929253899>", inline=True)
        embed.add_field(name="<a:system:859814116410523719> Banned word English", value="جلوگیری از فرستادن فحش های انگیلیسی و لاتین ایرانی\n وضعیت: <:deactive:859861439929253899>", inline=False)
        embed.add_field(name="<a:system:848585859459973152> Banned word Iran", value="جلوگیری از فرستادن فحش های ایرانی\n وضعیت: <:deactive:859861439929253899>", inline=False)
        embed.add_field(name="<a:locking:859814116410523719> Anti raid,nuck", value="جلوگیری از حملات به سرور\n وضعیت: <:deactive:859861439929253899>", inline=False)
        embed.add_field(name="<a:locking:859814116410523719> Banned Link", value="جلوگیری از فرستادن لینک های بد به سرور\n وضعیت: <:deactive:859861439929253899>", inline=False)
        embed.add_field(name="<a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100><a:lol:859811800441815100>", value="برای فعال سازی و خرید اشتراک در سرور ما عضو شوید", inline=False)
        embed.set_footer(text="Persiana Team\nDiscord:https://discord.gg/dE7JgUpa")
        await ctx.send(embed=embed)
          

@bot.command()
async def help(ctx, category=None):
    if ctx.guild.id in Servers:  
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="Persiana Bot v2<a:herp:859494461255974972>                             premium server: <:active:859823173968986112>", value=" <:kick:859808070347653151> چه طوری جون دل برقراری عزیز .سر کیفی بدم سر کیفی الکی دنبال کامند ها نگرد بیا همش اینجان", inline=False)
        embed.add_field(name="<a:system:848585859459973152> `!moderation`", value="برای مدیریت سرور خود از این کامند استفاده کرده و تمام کامند های ادمینی را ببین<a:yes:859493855410126868>", inline=False)
        embed.add_field(name="<a:Diamond:859097796278485032> `!public`", value=" تمام کامندهایی که هر باتی داره و نیاز شما عزیزان قوربونتون برم هست <a:herp2:859505382841516052>", inline=False)
        embed.add_field(name="<:kick:859808070347653151> `!fun`", value="    تمام کامند های شنگولی که می خوای تا کرم بریزی   <a:herp2:859505382841516052>", inline=False)
        embed.set_footer(text="Persiana Team")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="Persiana Bot<a:herp:859494461255974972>                             premium server: <:deactive:859861439929253899>", value=" <:kick:859808070347653151> چه طوری جون دل برقراری عزیز .سر کیفی بدم سر کیفی الکی دنبال کامند ها نگرد بیا همش اینجان", inline=False)
        embed.add_field(name="<a:system:848585859459973152> `!moderation`", value="برای مدیریت سرور خود از این کامند استفاده کرده و تمام کامند های ادمینی را ببین<a:yes:859493855410126868>", inline=False)
        embed.add_field(name="<a:Diamond:859097796278485032> `!public`", value=" تمام کامندهایی که هر باتی داره و نیاز شما عزیزان قوربونتون برم هست <a:herp2:859505382841516052>", inline=False)
        embed.set_footer(text="Persiana Team")
        await ctx.send(embed=embed)








@bot.command()
async def public(ctx, category=None):
    if ctx.guild.id in Servers:
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="Persiana Bot<a:herp:859494461255974972>                             premium server: <:active:859823173968986112>", value=" <:kick:859808070347653151> چه طوری جون دل برقراری عزیز .سر کیفی بدم سر کیفی الکی دنبال کامند ها نگرد بیا همش اینجان", inline=False)
        embed.add_field(name="`!id`", value="آیدی اکانت شما <:Dev:847030080516390962>", inline=False)
        embed.add_field(name="`!serverinfo`", value="اطلاعات سروری که الان داخلش هستی <a:LOL:860170058759798804>", inline=True)
        embed.add_field(name="`!serverlogo`", value="لوگو سروری که الان داخلش هستی <a:herp:859494461255974972>", inline=True)
        embed.add_field(name="`!info [شخص]`", value="اطلاعات شخص مورد نظر در این سرور <a:Ver:847030966614753301>", inline=True)
        embed.add_field(name="`!invites`", value="تعداد اینوایت های شما در این سرور <:Verify:847031254230630420>", inline=True)
        embed.add_field(name="`!roleinfo [role]`", value="اطلاعات در مورد رول مورد نظر  <a:verify:848584184258625596>", inline=True)
        embed.add_field(name="`!avatar [شخص]`", value="دیدن اواتار شخص مورد نظر<:kick:859808070347653151>", inline=True)
        embed.add_field(name="`!rank`", value="جهت نشان دادن لول و سطح شما در این سرور<a:can:848584162537242684>", inline=True)
        embed.set_footer(text="Persiana Team")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=0xf1c40f)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="Persiana Bot<a:herp:859494461255974972>                             premium server: <:deactive:859861439929253899>", value=" <:kick:859808070347653151> چه طوری جون دل برقراری عزیز .سر کیفی بدم سر کیفی الکی دنبال کامند ها نگرد بیا همش اینجان", inline=False)
        embed.add_field(name="`!id`", value="آیدی اکانت شما <:Dev:847030080516390962>", inline=False)
        embed.add_field(name="`!serverinfo`", value="اطلاعات سروری که الان داخلش هستی <a:LOL:860170058759798804>", inline=True)
        embed.add_field(name="`!serverlogo`", value="لوگو سروری که الان داخلش هستی <a:herp:859494461255974972>", inline=True)
        embed.add_field(name="`!info [شخص]`", value="اطلاعات شخص مورد نظر در این سرور <a:Ver:847030966614753301>", inline=True)
        embed.add_field(name="`!invites`", value="تعداد اینوایت های شما در این سرور <:Verify:847031254230630420>", inline=True)
        embed.add_field(name="`!roleinfo [role]`", value="اطلاعات در مورد رول مورد نظر  <a:verify:848584184258625596>", inline=True)
        embed.add_field(name="`!avatar [شخص]`", value="دیدن اواتار شخص مورد نظر<:kick:859808070347653151>", inline=True)
        embed.add_field(name="`!rank`", value="جهت نشان دادن لول و سطح شما در این سرور<a:can:848584162537242684>", inline=True)
        embed.set_footer(text="Persiana Team")
        await ctx.send(embed=embed)





#----------------------------------------------------------------------------------------------------
# public



@bot.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"<:Lol:847057619335905302> {len(ctx.guild.members)}members\n <:Lol:847057619335905302> {len(ctx.guild.roles)} roles\n <:s_:847125230127153204> {len(ctx.guild.text_channels)} Text-Channels\n <:s_:847125230127153204> {len(ctx.guild.voice_channels)} Voice-Channels\n <:Staff:847030024255307788> {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="<:oo:847123873383710730> Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="<:Verify:847031254230630420> Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="<:lol2:847118777867042847> Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="<:Dev:847030080516390962> Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@bot.command()
async def id(ctx):
    embed=discord.Embed(title="Persiana Team", description=f"<:Dev:847030080516390962> Your Developer ID : {ctx.author.id}", color=discord.Color.blue())
    await ctx.send(embed=embed)



@bot.command(description="Gets info about the user")
async def info(ctx ,user):
    user = ctx.author
    embed=discord.Embed(title="Your Info", description=f"Here You are {user}", colour=0x4146d1)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="<:Lol:847057619335905302> Name", value=user.name, inline=True)
    embed.add_field(name="<:Verify:847031254230630420> Nickname", value=user.nick, inline=True)
    embed.add_field(name="<:Dev:847030080516390962> ID", value=user.id, inline=True)
    embed.add_field(name="<:Verify:847031254230630420> Top role", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def invites(ctx, member:discord.Member=None):
      if member == None:
          member = ctx.message.author
      totalInvites = 0
      for i in await ctx.guild.invites():
          if i.inviter == member:
              totalInvites += i.uses
      embed=discord.Embed(title="Your Invites", description="**" + member.mention + " has invited `" + str(totalInvites) + " User` to `" + str(ctx.guild.name) + "`**", color=discord.Color.blue())
      await ctx.send(embed=embed)

@bot.command(aliases=['guildpfp'])
async def serverlogo(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)
    



@bot.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@bot.command()
async def fun(ctx, category=None):
    if category is None:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="Persiana Bot<a:herp:859494461255974972>                             premium server: <:active:859823173968986112>", value=" <:kick:859808070347653151> چه طوری جون دل برقراری عزیز .سر کیفی بدم سر کیفی الکی دنبال کامند ها نگرد بیا همش اینجان", inline=False)
        embed.add_field(name="`!kiss [شخص]`", value="<:kick:859808070347653151> ماچ کردن کسی", inline=True)
        embed.add_field(name="`!hug [شخص]`", value="<:kick:859808070347653151> بغل کردن کسی", inline=True)
        embed.add_field(name="`!slap [شخص]`", value="<:kick:859808070347653151> چک زدن ", inline=True)
        embed.add_field(name="`!cuddle [شخص]`", value="<:kick:859808070347653151> به مولا که", inline=True)
        embed.add_field(name="`!smug [شخص]`", value="<:kick:859808070347653151>  زدن کسی", inline=True)
        embed.add_field(name="`!punch [شخص]`", value="<:kick:859808070347653151> زدن کسی", inline=True)
        embed.add_field(name="`!shoot [شخص]`", value="<:kick:859808070347653151> به فنا دادن کسی", inline=True)
        embed.add_field(name="`!meme`", value="<:kick:859808070347653151> Meme", inline=True)
        embed.add_field(name="`!pat [شخص]`", value="<:kick:859808070347653151> ناز کردن کسی", inline=True)
        embed.add_field(name="`!dog`", value="<:kick:859808070347653151>  سگ", inline=True)
        embed.add_field(name="`!cat`", value="<:kick:859808070347653151> گربه", inline=True)
        embed.add_field(name="`!sadcat`", value="<:kick:859808070347653151> گربه غمگین", inline=True)
        embed.add_field(name="`!bird`", value="<:kick:859808070347653151>  پرنده", inline=True)
        embed.add_field(name="`!fox`", value="<:kick:859808070347653151>  روباه", inline=True)
        embed.add_field(name="`!duck`", value="<:kick:859808070347653151> اردک", inline=True)
        embed.set_footer(text="Coded By Persiana Team😋\nDiscord: https://discord.gg/7cRENBSnHp")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/834067226209943582/837352601325666314/958787.png")
        embed.add_field(name="Persiana Bot<a:herp:859494461255974972>                             premium server: <:deactive:859861439929253899>", value=" <:kick:859808070347653151> چه طوری جون دل برقراری عزیز .سر کیفی بدم سر کیفی الکی دنبال کامند ها نگرد بیا همش اینجان", inline=False)
        embed.add_field(name="`!kiss [شخص]`", value="<:kick:859808070347653151> ماچ کردن کسی", inline=True)
        embed.add_field(name="`!hug [شخص]`", value="<:kick:859808070347653151> بغل کردن کسی", inline=True)
        embed.add_field(name="`!slap [شخص]`", value="<:kick:859808070347653151> چک زدن ", inline=True)
        embed.add_field(name="`!cuddle [شخص]`", value="<:kick:859808070347653151> به مولا که", inline=True)
        embed.add_field(name="`!smug [شخص]`", value="<:kick:859808070347653151>  زدن کسی", inline=True)
        embed.add_field(name="`!punch [شخص]`", value="<:kick:859808070347653151> زدن کسی", inline=True)
        embed.add_field(name="`!shoot [شخص]`", value="<:kick:859808070347653151> به فنا دادن کسی", inline=True)
        embed.add_field(name="`!meme`", value="<:kick:859808070347653151> Meme", inline=True)
        embed.add_field(name="`!pat [شخص]`", value="<:kick:859808070347653151> ناز کردن کسی", inline=True)
        embed.add_field(name="`!dog`", value="<:kick:859808070347653151>  سگ", inline=True)
        embed.add_field(name="`!cat`", value="<:kick:859808070347653151> گربه", inline=True)
        embed.add_field(name="`!sadcat`", value="<:kick:859808070347653151> گربه غمگین", inline=True)
        embed.add_field(name="`!bird`", value="<:kick:859808070347653151>  پرنده", inline=True)
        embed.add_field(name="`!fox`", value="<:kick:859808070347653151>  روباه", inline=True)
        embed.add_field(name="`!duck`", value="<:kick:859808070347653151> اردک", inline=True)
        embed.set_footer(text="Coded By Persiana Team😋\nDiscord: https://discord.gg/7cRENBSnHp")




@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def duck(ctx):
    embed = discord.Embed(title="Quack!", description=" ", color=0x176cd5)
    embed.set_image(url="https://random-d.uk/api/v1/randomimg")
    await ctx.send(embed=embed)



@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def punch(ctx, member: discord.Member):
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://cdn.discordapp.com/attachments/843853101403865108/850457825393639424/507bd16df309b4fd7b5893fc3930f2de.gif")
    await ctx.send(embed=embed)

# shoot command
@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def shoot(ctx, member: discord.Member):
    embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await ctx.send(embed=embed)



@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kiss(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.botSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Persianakiss.gif"))
    except:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slap(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.botSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Persiana.gif"))
    except:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hug(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.botSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Persiana.gif"))
    except:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def cuddle(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.botSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Persiana.gif"))
    except:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def smug(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.botSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Persiana.gif"))
    except:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def pat(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.botSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Persiana.gif"))
    except:
        embed = discord.Embed(colour=0x4146d1)
        embed.set_author(name="Persiana Bot",
                         icon_url="https://cdn.discordapp.com/attachments/834067226209943582/847055972618862612/Persian-Team.png")
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)



@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def dog(ctx):
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.botSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Persiana.png"))
    except:
        await ctx.send(link)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def cat(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.botSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Persiana.png"))
    except:
        await ctx.send(link)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sadcat(ctx):
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.botSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Persiana.png"))
    except:
        await ctx.send(link)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def bird(ctx):
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.botSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Persiana.png"))
    except:
        await ctx.send(link)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def fox(ctx):
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.botSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Persiana.png"))
    except:
        await ctx.send(link)



bot.run(config.TOKEN)
