from discord.ext import commands

AUTHOR = None  # Ник#0001 аккаунта
ID = None  # id аккаунта

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Connected')


@client.command(pass_context=True)
async def l(ctx):
    AUTHOR = ctx.author
    ID = ctx.author.id
    await ctx.send(AUTHOR)
    await ctx.send(ID)


client.run("Njk0MjIzMjg0NTg1MTAzNDYw.XoI4pA.zvgQ1h_tkRjoyzLEI6CA5Ab0jYs")
