# discord dependencies
import discord
from discord.ext import commands

class GeneralExtension(commands.Cog):

	#constructor
	def __init__(self, bot):
		self.bot = bot

	# on startup
	# params: none
	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot is online and well. :)')

	# on error
	# params: client context, error instance
	@commands.Cog.listener()
	async def on_command_error(self, context, error):
		if isinstance(error, commands.CommandNotFound):
			await context.send('Command does not exist.')

	# >ping command
	# params: client context
	@commands.command()
	async def ping(self, context):
		"""Provides latency of this bot in milliseconds.\n
		Parameters: None | Example: '>ping'"""
		await context.send(F'{round(self.bot.latency * 1000)}ms')

# register this cog with bot when loaded
def setup(bot):
	try:
		bot.add_cog(GeneralExtension(bot))
		print('Successfully loaded general extension.')
	except Exception as e:
		sys.exit()