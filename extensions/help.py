from typing import Optional

# discord dependencies
import discord
from discord.ext import commands

class HelpExtension(commands.Cog):

	#constructor
	def __init__(self, bot):
		self.bot = bot
		self.commandset = set()
		for command in self.bot.commands:
			self.commandset.add(command.name)

	# placeholder for '>help help'
	# not intended but help is sometimes not recognized via bot.commands()
	# happens upon initial load or reload of extensions
	# params: client context
	async def helphelp(self, context):
		description = "Provide insight on how to use certain commands pertaining to this bot.\n\nParameters: (Optional) Command Name | Examples: \'>help covid\' or \'>help countries\'"
		embed = discord.Embed(
				title = '>help',
				colour = discord.Colour.dark_teal()
		)
		embed.add_field(name = 'Command description', value = description, inline = False)
		await context.send(embed = embed)

	# helper function for when >help is called without params
	# creates an embedded message with all possible user commands
	# params: client context, bot command object
	async def helpnone(self, context):
		embed = discord.Embed(
			title = F'Bot Commands',
			colour = discord.Colour.dark_teal()
		)
		embed.add_field(name = 'Covid-19 (covidstat)', value = '`covid`, `countries`, `cname`, `ccode`, `csource`', inline = False)
		embed.add_field(name = 'Miscellaneous (misc)', value = '`randomfox`', inline = False)
		embed.add_field(name = 'General (general)', value = '`ping`, `load`, `unload`', inline = False)
		embed.set_footer(text = 'For more information use >help (command) | Example: \'>help covid\' or \'>help countries\'')
		await context.send(embed = embed)

	# helper function for the help command
	# creates an embedded message awaiting client send
	# params: client context, bot command object
	async def helper(self, context, command):
		embed = discord.Embed(
			title = F'>{command.name}',
			colour = discord.Colour.dark_teal()
		)
		embed.add_field(name = 'Command description', value = command.help, inline = False)
		await context.send(embed = embed)

	# >help command
	# provide useful information regarding commands
	# params: client context, optional client-side command str
	@commands.command()
	async def help(self, context, cmd: Optional[str]):
		"""Provide insight on how to use certain commands pertaining to this bot.\n
		Parameters: {Optional} Command Name | Examples: '>help covid' or '>help countries'"""
		if cmd is None:
			await self.helpnone(context)
		elif cmd == 'help':
			await self.helphelp(context)
		else:
			if cmd in self.commandset:
				for command in self.bot.commands:
					if command.name == cmd:
						await self.helper(context, command)
						return
			else:
				await context.send(F'Command \'>{cmd}\' does not exist.')

# register this cog with bot when loaded
def setup(bot):
	try:
		bot.add_cog(HelpExtension(bot))
		print('Successfully loaded custom help extension.')
	except Exception as e:
		sys.exit()