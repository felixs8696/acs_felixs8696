import doctest

# Calculates a^b using only addition
def expFromAdd(a,b):
	"""Calculates a^b using only addition
    >>> expFromAdd(2,3)
    8
    >>> expFromAdd(5,5)
    3125
    """

doctest.testmod()