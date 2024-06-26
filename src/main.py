import discord
from discord.ext import commands, tasks
import datetime
import pytz

# Define your intents
intents = discord.Intents.default()

BOT_ID = "YOUR_BOT_ID"
YOUR_CHANNEL_ID = "YOUR_CHANNEL_ID"
bot = commands.Bot(command_prefix='?', intents=intents)

timezone = pytz.timezone('Asia/Ho_Chi_Minh')

# Dates for your tests (replace with your actual test dates)
speaking_test_date = timezone.localize(datetime.datetime(2024, 4, 19, 16, 45, 0))  # April 19th, 2024 at 4:45 PM
lrw_test_date = timezone.localize(datetime.datetime(2024, 4, 20, 9, 0, 0))  # April 20th, 2024 at 9:00 AM

def get_current_time():
    now = datetime.datetime.now(timezone)
    current_time = now.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return current_time

def get_days_left(test_date):
    now = datetime.datetime.now(timezone)
    delta = test_date - now
    return delta.days

def format_message(days_left, test_name, user_id):
    mention = f"<@{user_id}>"
    if days_left == 0:
        return f"{mention} Today is your {test_name} test day!"
    elif days_left == 1:
        return f"{mention} Only 1 day left until your {test_name} test!"
    else:
        return f"{mention} Only {days_left} days left until your {test_name} test!"

@bot.command()
async def speaking(ctx):
    current_time = get_current_time()
    await ctx.send(f"The current time for your speaking test is: {current_time}")

@bot.command()
async def lrw(ctx):
    current_time = get_current_time()
    await ctx.send(f"The current time for your listening, reading, writing test is: {current_time}")

@tasks.loop(hours=24)
async def announce_days_left():
    speaking_days_left = get_days_left(speaking_test_date)
    lrw_days_left = get_days_left(lrw_test_date)

    channel = bot.get_channel(int(YOUR_CHANNEL_ID))

    # Replace USER_ID with the actual user ID you want to tag
    user_id = "USER_ID"

    await channel.send(format_message(speaking_days_left, "Speaking", user_id))
    await channel.send(format_message(lrw_days_left, "Listening, Reading, Writing", user_id))

@bot.event
async def on_ready():
    print(f"I am inside {bot.user.name}!")
    announce_days_left.start()

bot.run('YOUR_BOT_ID')
