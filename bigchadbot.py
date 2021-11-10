import discord
import random
import asyncpraw


reddit1 = asyncpraw.Reddit(client_id = "GGj6f657ASp5KYtTU-HxJw",
                     client_secret = "RGFyym8y8tRkfarv3wJpaba2ui7DZA",
                     username = "bigchadtest",
                     password = "v26102002",
                     user_agent="bigchadtest")

from discord.ext import commands  
intents = discord.Intents.default()
intents.members = True  
client = commands.Bot(command_prefix = '<', intents=intents)

@client.event
async def on_ready():
    print('The Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency*1000}')

@client.command(aliases = ['8ball', 'fortune'])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.",
                 "Ask again later.", 
                 "Better not tell you now.",
                 "Cannot predict now.", 
                 "Concentrate and ask again.",
                 "Don’t count on it.", 
                 "It is certain.", 
                 "It is decidedly so.", 
                 "Most likely.", 
                 "My reply is no.", 
                 "My sources say no.",
                 "Outlook not so good.", 
                 "Outlook good.", 
                 "You can't handle the truth.", 
                 "Signs point to yes.", 
                 "Very doubtful.", 
                 "Without a doubt.",
                 "Yes.", 
                 "Yes – definitely.", 
                 "You may rely on it."]
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')

@client.command(aliases = ['sigma', 'sigmarule'])
async def sigmarules(ctx):
    await ctx.send("<a:gigachad:906765600221720616>")
    subreddit = await reddit1.subreddit("SigmaGrindset")
    all_subs = []
    sigma = subreddit.top(limit=250)

    async for submission in sigma:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    emsigma = discord.Embed(title = name, colour = discord.Colour.random(), url = url)
    emsigma.set_image(url = url)

    await ctx.send(embed = emsigma)

@client.command(aliases = ['meme', 'dank'])
async def memes(ctx):
    await ctx.send("Loading da meme <:catloading:906788419647197214>")
    subreddit = await reddit1.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 250)

    async for submission in top:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, colour = discord.Colour.random(), url = url)
    em.set_image(url = url)
    
    em.set_footer(text = "Here is your damn meme, now chill!")
    await ctx.send(embed = em)

@client.command(name = "holup")
async def memes(ctx):

    subreddit = await reddit1.subreddit("holup")
    all_subs = []
    top = subreddit.top(limit = 250)

    async for submission in top:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, colour = discord.Colour.random(), url = url)
    em.set_image(url = url)
    
    em.set_footer(text = "Don't be surprised, it is what it is ¯\_(ツ)_/¯")
    await ctx.send(embed = em)

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit = amount)
    
@client.command()
async def kick(ctx, member : discord.Member, *,reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"Ha!, Pro Move for kicking {member.mention}")

@client.command()
async def ban(ctx, member : discord.Member, *,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Ha!, Pro Move for banning {member.mention}")

@client.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans() #returns list, thus async for can't be used
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Ahh!, Nevermind, unbanned {user.mention} <")
            return

client.run(os.getenv('TOKEN'))
