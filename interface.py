import enum

class Result(enum.Enum):
	MISS	= enum.auto()
	DAMAGE	= enum.auto()
	KILL	= enum.auto()
	WIN		= enum.auto()
