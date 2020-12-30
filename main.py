import sys
import os

# discord dependencies
import discord
from discord.ext import commands

# bot trigger string
bot = commands.Bot(command_prefix = '>')

# remove discords default help command
bot.remove_command('help')\

# load extension
# params: client context, extension filename
@bot.command()
async def load(context, functionality):
	try:
		bot.load_extension(F'extensions.{functionality}')
		await context.send(F'{functionality} commands are now enabled.')
	except Exception as e:
		await context.send(F'Extension: {functionality} does not exist.')

# unload extension
# params: client context, extension filename
@bot.command()
async def unload(context, functionality):
	try:
		bot.unload_extension(F'extensions.{functionality}')
		await context.send(F'{functionality} commands are now disabled.')
	except Exception as e:
		await context.send(F'Extension: {functionality} does not exist.')	

# load all extensions / cogs and their respective commands
try:
	for filename in os.listdir('./extensions'):
		if filename.endswith('.py'):
			bot.load_extension(F'extensions.{filename[:-3]}')
except Exception as e:
	print(F'Ran into unexpected error: {e.__class__.__name__}')
	sys.exit()

# PASTE TOKEN HERE
token = ''

# run with token
bot.run(token)