"""

"""
from os import getenv


class EnvironmentError(Exception):
	pass


class EnvironmentVariableError(EnvironmentError):
	pass


class MissingEvironmentVariableError(EnvironmentVariableError):
	def __init__(self, key):
		message = ''.join({ENV_PREFIX, key})
		super(EnvironmentVariableError, self).__init__(self, message)


class EnvironmentVariables(object):
	"""
	"""

	def __init__(self, prefix=""):
		self.prefix = prefix

	def _get(self, key, default=None, required=False):
		full_key = ''.join({self.prefix, key})
		value = getenv(full_key, default)
		if required and not value:
			raise MissingEvironmentVariableError(full_key)
		return value

	def load(self, var_list):
		raise Exception('Set up EnvironmentVariables')


class DatabaseSettings(object):
	"""
	Load those database settings, yo!
	"""
	def __init__():
		pass

