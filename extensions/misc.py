import requests
import random

# discord dependencies
import discord
from discord.ext import commands

class MiscExtension(commands.Cog):

	# constructor
	def __init__(self, bot):
		self.bot = bot

	# >randomfox command
	# returns image url of fox(es)
	# source: https://randomfox.ca/
	# params: client context
	@commands.command()
	async def randomfox(self, context):
		"""Provides random image of fox.\n
		Parameters: None | Example: '>randomfox'"""
		response = requests.get("https://randomfox.ca/floof")
		fox = response.json()
		await context.send(fox['image'])

# register this cog with bot when loaded
def setup(bot):
	try:
		bot.add_cog(MiscExtension(bot))
		print('Successfully loaded misc extension.')
	except Exception as e:
		sys.exit()