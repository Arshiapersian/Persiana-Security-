import discord
from discord.ext import commands
import aiosqlite
import math
import random
import aiohttp
import io
from PIL import Image, ImageDraw, ImageFont




class Levelling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = None
        self.bot.loop.create_task(self.connect_database())

    async def connect_database(self):
        self.db = await aiosqlite.connect('database.db')

    async def find_or_insert_user(self, member: discord.Member):
        # user_id, guild_id, xp, level
        cursor = await self.db.cursor()
        await cursor.execute('Select * from users where user_id = ?', (member.id,))
        result = await cursor.fetchone()
        if result is None:
            result = (member.id, member.guild.id, 0, 0)
            await cursor.execute('Insert into users values(?, ?, ?, ?)', result)
            await self.db.commit()

        return result

    def calculate_xp(self, level):
        return 100 * (level ** 2)

    def calculate_level(self, xp):
        # Sqrt => value ** 0.5
        return round(0.1 * math.sqrt(xp))


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot is True or message.guild is None:
            return

        result = await self.find_or_insert_user(message.author)

        user_id, guild_id, xp, level = result
        #print(xp, level)

        xp += random.randint(10, 40)
        
        if self.calculate_level(xp) > level:
            level += 1
            # 1,000
            await message.channel.send(f"{message.author.mention} افرین , خسته نباشی  شما به سطح  [{level:,}] رفتی <a:Diamond:859097796278485032>") 

        cursor = await self.db.cursor()
        await cursor.execute('Update users set xp=?, level=? where user_id=? and guild_id=?', (xp, level, user_id, guild_id))
        await self.db.commit()

    async def make_rank_image(self, member: discord.Member, rank, level, xp, final_xp):
        user_avatar_image = str(member.avatar_url_as(format='png', size=1024))
        async with aiohttp.ClientSession() as session:
            async with session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())


        img = Image.new('RGB', (1000, 240), (28, 40, 51))
        logo = Image.open(avatar_bytes).resize((125, 125))

        # Stack overflow helps :)
        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)
        ##############################
        img.paste(logo, (5, 5), mask=logo)

        # Black Circle
        draw = ImageDraw.Draw(img, 'RGB')
        draw.ellipse((152, 152, 208, 208), fill='#fff')

        # Placing offline or Online Status
        # Discord Colors (Online: '#43B581')
        draw.ellipse((155, 155, 205, 205), fill='#02ad21')
        ##################################

        # Working with fonts
        big_font = ImageFont.FreeTypeFont('arshiafont.otf', 60)
        medium_font = ImageFont.FreeTypeFont('arshiafont.otf', 40)
        small_font = ImageFont.FreeTypeFont('arshiafont.otf', 30)
        Persiana_font = ImageFont.FreeTypeFont('nicefont.ttf', 60)
        Persiana2_font = ImageFont.FreeTypeFont('amir.otf', 40)
        Persiana23_font = ImageFont.FreeTypeFont('nicefont.ttf', 40)
        #####
        img = Image.open("ars.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        img = Image.new('RGB', (1000, 240), (28, 40, 51))
        logo = Image.open(avatar_bytes).resize((125, 125))
        img = Image.open("ars.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)

        # Stack overflow helps :)
        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)
        ##############################
        img.paste(logo, (5, 5), mask=logo)

        # Black Circle
        draw = ImageDraw.Draw(img, 'RGB')
      #  draw.ellipse((152, 152, 208, 208), fill='#fff')

        # Placing offline or Online Status
        # Discord Colors (Online: '#43B581')
        #draw.ellipse((155, 155, 205, 205), fill='#02ad21')
       # draw.ellipse((152, 152, 208, 208), fill='#fff')
       # draw.ellipse((155, 155, 205, 205), fill='#02ad21')

       # text_size = draw.textsize("", font=small_font)
       # offset_x = 525-15 - text_size[0]
       # offset_y = 45 
       # draw.text((offset_x, offset_y), "", font=Persiana_font, fill="#0f0f0f")
       # text_size = draw.textsize('', font=Persiana_font)

       # offset_x -= 370 + text_size[0]
       # offset_y = 2
        #draw.text((offset_x, offset_y), "Persiana Community", font=Persiana_font, fill="#0f0f0f")


        # Placing Level text (right-upper part)
        text_size = draw.textsize(f"{level}", font=big_font)
        offset_x = 1000-15 - text_size[0]
        offset_y = 5 
        draw.text((offset_x, offset_y), f"{level}", font=big_font, fill="#ffff12")
        text_size = draw.textsize('Level', font=small_font)

        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "Level", font=small_font, fill="#ffff12")

        # Placing Rank Text (right upper part)
        text_size = draw.textsize(f"#{rank}", font=big_font)
        offset_x -= 15 + text_size[0]
        offset_y = 8
        draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#ffff12")

        text_size = draw.textsize("Rank", font=small_font)
        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "Rank", font=small_font, fill="#ffff12")

        # Placing Progress Bar
        # Background Bar
        bar_offset_x = logo.size[0] + 20 + 9
        bar_offset_y = 170
        bar_offset_x_1 = 900 - 30
        bar_offset_y_1 = 200
        circle_size = bar_offset_y_1 - bar_offset_y

        # Progress bar rect greyier one
        draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#fff")
        # Placing circle in progress bar

        # Left circle
        draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#fff")

        # Right Circle
        draw.ellipse((bar_offset_x_1 - circle_size//2, bar_offset_y, bar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#fff")


#727175

#11ebf2
        # Filling Progress Bar

        bar_length = bar_offset_x_1 - bar_offset_x
        # Calculating of length
        # Bar Percentage (final_xp - current_xp)/final_xp

        # Some variables
        progress = (final_xp - xp) * 100/final_xp
        progress = 100 - progress
        progress_bar_length = round(bar_length * progress/100)
        pbar_offset_x_1 = bar_offset_x + progress_bar_length

        # Drawing Rectangle
        draw.rectangle((bar_offset_x, bar_offset_y, pbar_offset_x_1, bar_offset_y_1), fill="#fbff12")
        # Left circle
        draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#fbff12")
        # Right Circle
        draw.ellipse((pbar_offset_x_1 - circle_size//2, bar_offset_y, pbar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#fbff12")


        def convert_int(integer):
            integer = round(integer / 1000, 2)
            return f'{integer}K'

        # Drawing Xp Text
        text = f"/ {convert_int(final_xp)} Xp"
        xp_text_size = draw.textsize(text, font=small_font)
        xp_offset_x = bar_offset_x_1 - xp_text_size[0]
        xp_offset_y = bar_offset_y - xp_text_size[1] - 10
        draw.text((xp_offset_x, xp_offset_y), text, font=small_font, fill="#fff")

        text = f'{convert_int(xp)} '
        xp_text_size = draw.textsize(text, font=small_font)
        xp_offset_x -= xp_text_size[0]
        draw.text((xp_offset_x, xp_offset_y), text, font=small_font, fill="#fff")

        # Placing User Name
        text = member.display_name
        text_size = draw.textsize(text, font=Persiana23_font)
        text_offset_x = bar_offset_x - 10
        text_offset_y = bar_offset_y - text_size[1] - 10
        draw.text((text_offset_x, text_offset_y), text, font=Persiana23_font, fill="#fff")

        # Placing Discriminator
        text = f'#{member.discriminator}'
        text_offset_x += text_size[0] + 10
        text_size = draw.textsize(text, font=small_font)
        text_offset_y = bar_offset_y - text_size[1] - 10
        draw.text((text_offset_x, text_offset_y), text, font=small_font, fill="#fff")

        bytes = io.BytesIO()
        img.save(bytes, 'PNG')
        bytes.seek(0)
        return bytes
        
    

    @commands.command()
    async def rank(self, ctx: commands.Context, member: discord.Member=None):
        member = member or ctx.author
        cursor = await self.db.cursor()
        user = await self.find_or_insert_user(member)
        user_id, guild_id, xp, level = user
        await cursor.execute("Select Count(*) from users where xp > ? and guild_id=?", (xp, guild_id))
        result = await cursor.fetchone()
        rank = result[0] + 1
        final_xp = self.calculate_xp(level + 1)
        bytes = await self.make_rank_image(member, rank, level, xp, final_xp)
        file = discord.File(bytes, 'rank.png')
        await ctx.send(file=file)


    @commands.command(aliases=["av", "pfp"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:member=ctx.message.author

        message = discord.Embed(title=str(member), color=discord.Color.blue())
        message.set_image(url=member.avatar_url)

        await ctx.send(embed=message)



def setup(bot):
    bot.add_cog(Levelling(bot))