import discord
from discord.ext import commands
import os
import asyncio
from discord.flags import Intents
from stay_online import stay_online

# Imports added for adding Email Verification
import sqlite3
import re
import random
import yagmail
import requests

yag = yagmail.SMTP(os.getenv('EMAIL'), os.getenv('PASSWORD'))


client = discord.Client()
client = commands.Bot(status=discord.Status.dnd, command_prefix= "=", intents = discord.Intents.all())

client.remove_command("help")

# Login prompt for the Bot and varying Rich Presence
@client.event
async def on_ready():
    print('{0.user} is now up and running!'.format(client))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = "HelloIITK Lectures :) | =help"))
        await asyncio.sleep(20)

        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = f"students of {len(client.guilds)} IITK servers get dassa | =help"))
        await asyncio.sleep(20)

        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = f"{sum([len(guild.members) for guild in client.guilds])} students get a dassa | =help"))
        await asyncio.sleep(20)

        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = "Online Convocation | =help"))
        await asyncio.sleep(20)

# Main Help Command
@client.group(invoke_without_command=True)
async def help(ctx):
    help=discord.Embed(title="IITK Bot Help", color=0x00ff00, description="My prefix is `=`, and commands are to be run as `=<command name>`. Here goes a list of my commands. Use `=help <command name>` to know more about a specific command")
    help.set_author(name="IITK Bot", url="https://github.com/QuantuMAtharva/IITK-Bot", icon_url="https://media.discordapp.net/attachments/864451366327549963/865133614776451072/9k.png")
    help.set_footer(text="Powered by mooKIT", icon_url="https://cdn.discordapp.com/attachments/864451366327549963/865132951251451914/2Q.png")
    help.set_thumbnail(url="https://cdn.discordapp.com/attachments/864451366327549963/865132277620539402/iitk_logo.jpg")
    help.add_field(inline=False, name="Utility Commands", value="1. `iitk` : Gives important official websites related to IITK\n2. `snt` : Gives Server links for all SnT Clubs, with few other details\n3. `mnc` : Gives links related to MnC Clubs\n4. `acads` : Gives important links related to Academic things, like Grade Calculator Website, Course Resorces Links etc.")
    help.add_field(inline=False, name="Enabling IITK Email Verfication for the server", value="Use `=vstatus` to get started")
    help.add_field(inline=False, name="Extra Commands", value="1. `=clear <number>` : To clear a certain number of messages in a channel **[NOTE: Requires user to have Manage Messages Permission]**\n2. `=invite` : Get invite link for the Bot in your DM")
    await ctx.send(embed = help)

# Subcommands under the main help command
@help.command()
async def iitk(ctx):
    iitk = discord.Embed(title="`=iitk` Command", color=0x00ff00, description="Gives out links for IITK website, DoAA, DoSA, IITK Alumni Association, SIIC and much more...")
    await ctx.send(embed=iitk)

@help.command()
async def snt(ctx):
    snt = discord.Embed(title="`=snt` Command", color=0x00ff00, description="Gives out links for all SnT Club servers, websites etc along with much more details")
    await ctx.send(embed=snt)

@help.command()
async def mnc(ctx):
    mnc = discord.Embed(title="`=mnc` Command", color=0x00ff00, description="Gives out links for MnC Club servers, handles etc along with much more details")
    await ctx.send(embed=mnc)

@help.command()
async def acads(ctx):
    acads = discord.Embed(title="`=acads` Command", color=0x00ff00, description="Gives out important links related to Academic things, like Grade Calculator Website, Course Resources Links, Previous Batches Course Grades Stats etc.")
    await ctx.send(embed=acads)

@help.command()
async def clear(ctx):
    clear= discord.Embed(title="`=clear <number>` Command", color=0x00ff00, description="Clears a certain number of messages in a channel.\nUsage: `=clear 2` clears 2 latest messages\n**[NOTE: Requires user to have Manage Messages Permission]**")
    await ctx.send(embed=clear)

# Other Custom Commands
@client.command()
async def iitk(ctx):
    iitk_links=discord.Embed(title="Links related to IITK", color=0x00ff00, description="1. [IITK Website](https://www.iitk.ac.in)\n2. [IITK Alumni Association](https://iitkalumni.org/)\n3. [SIIC](https://siicincubator.com/)")
    await ctx.send(embed=iitk_links)

@client.command()
async def snt(ctx):
    snt_links=discord.Embed(title="Links related to SnT", color=0x00ff00, description="1. [SnT Website](https://www.sntiitk.in)\n2. [SnT Discord Server](https://discord.gg/ChYB82A49Y)")
    await ctx.send(embed=snt_links)

@client.command()
async def mnc(ctx):
    mnc_links=discord.Embed(title="Links related to MnC", color=0x00ff00, description="1. [MnC Website](https://students.iitk.ac.in/mnc/)")
    await ctx.send(embed=mnc_links)

@client.command()
async def acads(ctx):
    acads_links=discord.Embed(title="Links related to Academics", color=0x00ff00, description="1. [CPI/SPI Calculator](https://cpi-spi-calculator.herokuapp.com/)\n2. [Course Resorces Links](https://examvault.github.io) **(More coming soon)**\n3. [Faculty Wise Past Grades](https://incog-nahito.github.io/grades/faculty/) **|** [Course Wise Past Grades](https://grades-card.github.io/)")
    await ctx.send(embed=acads_links)

@client.command()
async def invite(ctx):
    invite_link = discord.Embed(title="Hi! I hope ||Chill Hai|| :slight_smile:.\nWant to invite me to your server?", color=0x00ff00, description="[Click Here](https://discord.com/api/oauth2/authorize?client_id=864761267687653416&permissions=8&scope=bot) to Invite me!")
    await ctx.author.send(embed=invite_link)

@client.command()
async def bt(ctx):
    f = open("images.txt", "r")
    link = f.readlines()
    f.close()
    num = random.randint(0,10)
    bt = discord.Embed(title="You asked for it!" , color=0x00ff00)
    bt.set_image(url="{}".format(link[num]))
    bt.set_footer(text="Credits: Photography Club, IITK", icon_url="https://media.discordapp.net/attachments/875806171125133343/875813077839384576/19756849_2345530779006349_3968530115160506135_n.png?width=468&height=468")
    await ctx.send(embed=bt)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num=2):
    await ctx.channel.purge(limit = num+1)

# Command to enable email verification in a server

conn = sqlite3.connect('iitk_bot.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS 
users(
    userid INT,
    guildid INT, 
    email TEXT,
    code INT, 
    verified INTEGER);""")
c.execute("""CREATE TABLE IF NOT EXISTS
guilds(
    guildid INT PRIMARY KEY,
    domains TEXT,
    onjoin INT,
    role TEXT);""")
conn.commit()

# Fetch basic parameters
def get_guild(guildid):
    return c.execute("SELECT * FROM guilds WHERE guildid=?", (guildid,)).fetchone()

def new_guild(guildid, domains="", onjoin=0, role="IITK_Verified"):
    c.execute("INSERT INTO guilds VALUES (?, ?, ?, ?)", (guildid, domains, onjoin, role))
    conn.commit()

def get_user_guild(guildid, userid):
    return c.execute("SELECT * FROM users WHERE guildid=? AND userid=?", (guildid, userid)).fetchone()

def get_users_guilds(userid):
    return c.execute("SELECT * FROM users WHERE userid=?", (userid,)).fetchall()

def get_emails_guilds(guildid, email):
    return c.execute("SELECT * FROM users WHERE guildid=? AND email=? AND verified=1", (guildid, email)).fetchall()

def get_users_codes(userid, code):
    return c.execute("SELECT * FROM users WHERE userid=? AND code=?", (userid, code)).fetchall()

def verify_msg(guildname, domains):
    if domains == "":
        return "{} hasn't setup this bot yet.".format(guildname)
    else: 
        return "To verify yourself on {}, **reply here with your @{} email address**.".format(guildname, domains)

def new_user(userid, guildid, email="", code=0, verified=0):
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (userid, guildid, email, code, verified))
    conn.commit()

def verify_user(userid, guildid):
    c.execute("UPDATE users SET verified=1 WHERE userid=? AND guildid=?", (userid, guildid))
    conn.commit()

def get_domains(guildid):
    return get_guild(guildid)[1]

def add_domain(domain, guildid):
    d_get = get_domains(guildid)
    prevdomains = []
    if d_get != "":
        prevdomains = get_domains(guildid).split('|')
    if domain not in prevdomains:
        prevdomains.append(domain)
        c.execute("UPDATE guilds SET domains=? WHERE guildid=?", ('|'.join(prevdomains), guildid))
        conn.commit()

def remove_domain(domain, guildid):
    prevdomains = get_domains(guildid).split('|')
    if domain in prevdomains:
        prevdomains.remove(domain)
        c.execute("UPDATE guilds SET domains=? WHERE guildid=?", ('|'.join(prevdomains), guildid))
        conn.commit()

def change_role(role, guildid):
    c.execute("UPDATE guilds SET role=? WHERE guildid=?", (role, guildid))
    conn.commit()

def enable_onjoin(guildid):
    c.execute("UPDATE guilds SET onjoin=? WHERE guildid=?", (1, guildid))
    conn.commit()

def disable_onjoin(guildid):
    c.execute("UPDATE guilds SET onjoin=? WHERE guildid=?", (0, guildid))
    conn.commit()

def insert_code(code, userid, guildid):
    c.execute("UPDATE users SET code=? WHERE userid=? AND guildid=?", (code, userid, guildid))
    conn.commit()

def insert_email(email, userid, guildid):
    c.execute("UPDATE users SET email=? WHERE userid=? AND guildid=?", (email, userid, guildid))
    conn.commit()

def email_check(email):
    regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    if re.search(regex, email):
        return True
    else:
        return False


# Now commands and actions based on user joining the server/present in the server

# Check, create and add role to new users
@client.event
async def on_member_join(member):
    check_on_join = get_guild(member.guild.id)
    if check_on_join == None:
        new_guild(member.guild.id)
    elif check_on_join[2] == 1:
        user_prev_verify = get_user_guild(member.guild.id, member.id)
        if user_prev_verify == None:
            await member.send(verify_msg(member.guild, check_on_join[1]))
            new_user(member.id, member.guild.id)
        elif user_prev_verify[4] == 0:
            await member.send(verify_msg(member.guild, check_on_join[1]))
        elif user_prev_verify[4] == 1:
            role = discord.utils.get(member.guild.roles, name=check_on_join[3])
            if role:
                if role not in member.roles:
                    await member.add_roles(role)
            else:
                await member.guild.create_role(name=check_on_join[3])
                role = discord.utils.get(member.guild.roles, name=check_on_join[3])
                await member.add_roles(role)

# The email verification process
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_content = message.content.strip()
    if (message.guild == None) and email_check(message_content):
        users_guilds = get_users_guilds(message.author.id)
        if len(users_guilds) >= 1:
            guild_list = [i[1] for i in users_guilds if i[4] == 0]
            verif_list = []
            for i in guild_list:
                email_guild = get_emails_guilds(i, message_content)
                if len(email_guild) > 0:
                    continue
                guild_domains = get_domains(i)
                if len(guild_domains) == 0:
                    continue
                guild_domains = guild_domains.split('|')
                if message_content.split("@")[1] in guild_domains:
                    verif_list.append(i)
            if len(verif_list) >= 1:
                random_code = random.randint(100000, 999999)
                for i in verif_list:
                    insert_code(random_code, message.author.id, i)
                    insert_email(message_content, message.author.id, i)
                
                receiver = message_content
                body = str(random_code)

                try:
                  yag.send(
                    to=receiver,
                    subject="[IITK Bot] Verify your server email",
                    contents='<h1 style="text-align:center;">DM the Code below to the bot to verify yourself</h1>\n' + '<h3 style="text-align:center;">'+body+'</h3>',
                )
                  await message.channel.send("Email sent. **Reply here with your verification code**. If you haven't received it, check your spam folder.\nIf you still are not able to get the Verification Code, simply message the Email ID once again to retry")

                except Exception as e:
                  print(e)
                  await message.channel.send("Email failed to send")

                # Cancel the SendGrid approach
                
                # emailmessage = Mail(
                #     from_email=os.getenv('SENDGRID_EMAIL'),
                #     to_emails=message_content,
                #     subject='[IITK Bot] Verify your server email',
                #     html_content=str(random_code))
                # try:
                #     sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
                #     response = sg.send(emailmessage)
                #     print(response.status_code)
                #     print(response.body)
                #     print(response.headers)
                #     await message.channel.send("Email sent. **Reply here with your verification code**. If you haven't received it, check your spam folder.")
                # except Exception as e:
                #     print(e)
                    # mailgun_email = mailgun_send(message_content, random_code)
                    # if mailgun_email.status_code == 200:
                    #     await message.channel.send("Email sent. **Reply here with your verification code**. If you haven't received it, check your spam folder.")
                # else:
                #     await message.channel.send("Email failed to send.")


        else:
            await message.channel.send("You have not joined a server")
    elif (len(message_content) == 6) and message_content.isdigit():
        verif_code = int(message_content)
        prev_codes_f = get_users_codes(message.author.id, verif_code)
        prev_codes_g = [i for i in prev_codes_f if i[4] == 0]
        prev_codes = []
        for i in prev_codes_g:
            user_emails = get_emails_guilds(i[1], i[2])
            if len(user_emails) >= 1:
                continue
            else:
                prev_codes.append(i)
        if len(prev_codes) >= 1:
            for i in prev_codes:
                verify_user(message.author.id, i[1])
                curr_guild = client.get_guild(i[1])
                guild_db = get_guild(i[1])
                role = discord.utils.get(curr_guild.roles, name=guild_db[3])
                if role:
                    member = curr_guild.get_member(message.author.id)
                    if role not in member.roles:
                        await member.add_roles(role)
                else:
                    await curr_guild.create_role(name=guild_db[3])
                    role = discord.utils.get(curr_guild.roles, name=guild_db[3])
                    member = curr_guild.get_member(message.author.id)
                    await member.add_roles(role)
                await message.channel.send("You have been successfully verified on " + client.get_guild(i[1]).name)
        else:
            await message.channel.send("Incorrect code")
    elif message.guild == None:
        await message.channel.send("Invalid email")
    await client.process_commands(message)

# Get guild details
@client.event
async def on_guild_join(guild):
    check_on_join = get_guild(guild.id)
    if check_on_join == None:
        new_guild(guild.id)

# Change name of the Verified Role
@client.command()
async def rolechange(ctx, role=None):
    if role and ctx.guild and ctx.author.guild_permissions.administrator:
        role = role.strip()
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        check_on_join = get_guild(ctx.guild.id)
        role_d = discord.utils.get(ctx.guild.roles, name=check_on_join[3])
        if role_d:
            await role_d.edit(name=role)
            change_role(role, ctx.guild.id)
            await ctx.send("```Verified role: " + get_guild(ctx.guild.id)[3] + "```")
        else:
            role_d2 = discord.utils.get(ctx.guild.roles, name=role)
            if role_d2:
                change_role(role, ctx.guild.id)
                await ctx.send("```Verified role: " + get_guild(ctx.guild.id)[3] + ".```")
            else:
                await ctx.guild.create_role(name=role)
                change_role(role, ctx.guild.id)
                await ctx.send("```Verified role: " + get_guild(ctx.guild.id)[3] + ".```")

# Add the email domain required for verification of the users
@client.command()
async def domainadd(ctx, domain=None):
    if domain and ctx.guild and ctx.author.guild_permissions.administrator:
        domain = domain.strip()
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        add_domain(domain, ctx.guild.id)
        await ctx.send("```Current email domains: " + get_domains(ctx.guild.id) + "```")

# Remove the email domain required for verification of the users
@client.command()
async def domainremove(ctx, domain=None):
    if domain and ctx.guild and ctx.author.guild_permissions.administrator:
        domain = domain.strip()
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        remove_domain(domain, ctx.guild.id)
        await ctx.send("```Current email domains: " + get_domains(ctx.guild.id) + "```")

# Enable user verification on join
@client.command()
async def enableonjoin(ctx):
    if ctx.guild and ctx.author.guild_permissions.administrator:
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        enable_onjoin(ctx.guild.id)
        await ctx.send("```Verify when a user joins? - True```")

# Disable user verification on join
async def disableonjoin(ctx):
    if ctx.guild and ctx.author.guild_permissions.administrator:
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        disable_onjoin(ctx.guild.id)
        await ctx.send("```Verify when a user joins? - False```")

# The Email Verification Help message
@client.command()
async def vstatus(ctx):
    if ctx.guild:
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        check_on_join = get_guild(ctx.guild.id)
        on_join = bool(check_on_join[2])

        embed = discord.Embed(title="Email Verification Functionality Status", color=0x00ff00, description="Ping: " + "{0}ms".format(round(client.latency * 1000)) + "\n" +
            "User commands: " + "\n" +
            "   1. `=verify` : Sends a DM to the user to verify their email" + "\n" +
            "   2. `=vstatus` : This Status Embed" + "\n\n" +
            "Admin commands: " + "\n" +
            " - A domain must be added before users can be verified." + "\n" +
            " - **Use `=rolechange` instead of server settings to change the name of the verified role.**" + "\n\n" +
            "   1. `=enableonjoin` : Enables verifying users on join" + "\n" +
            "   2. `=disableonjoin` : Disables verifying users on join" + "\n" +
            "   3. `=domainadd domain` : Adds an email domain" + "\n" +
            "   4. `=domainremove domain` : Removes an email domain" + "\n" +
            "   5. `=rolechange role` : Changes the name of the verified role" + "\n\n" +
            "**Domains:** " + check_on_join[1] + "\n\n" + 
            "Verify when a user joins? (default = **False**): " + "**" + str(on_join) + "** (Current state)\n" + 
            "Verified role (default = **IITK_Verified**): " + "**" + check_on_join[3] + "** (Current State)")
        await ctx.send(embed=embed)


# Check latency
@client.command()
async def vping(ctx):
    await ctx.send("{0}ms".format(round(client.latency * 1000)))

# Send a DM to the user to verify their email
@client.command()
async def verify(ctx):
    if ctx.guild:
        check_on_join = get_guild(ctx.guild.id)
        if check_on_join == None:
            new_guild(ctx.guild.id)
        check_on_join = get_guild(ctx.guild.id)
        user_prev_verify = get_user_guild(ctx.guild.id, ctx.author.id)
        if user_prev_verify == None:
            new_user(ctx.author.id, ctx.guild.id)
            await ctx.author.send(verify_msg(ctx.guild, check_on_join[1]))
        elif user_prev_verify[4] == 0:
            await ctx.author.send(verify_msg(ctx.guild, check_on_join[1]))



stay_online()
client.run(os.getenv('TOKEN'))