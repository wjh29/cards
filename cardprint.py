# -*- coding: utf-8 -*-
#Austin
cardStrs = [
"""
----------
|A       |
|        |
|    ♠   |
|        |
|       A|
----------
""",
"""
----------
|2   ♠   |
|        |
|        |
|        |
|    ♠  2|
----------
""",
"""
----------
|3   ♠   |
|        |
|    ♠   |
|        |
|    ♠  3|
----------
""",
"""
----------
|4 ♠   ♠ |
|        |
|        |
|        |
|  ♠   ♠4|
----------
""",
"""
----------
|5 ♠   ♠ |
|        |
|    ♠   |
|        |
|  ♠   ♠5|
----------
""",
"""
----------
|6 ♠   ♠ |
|        |
|  ♠   ♠ |
|        |
|  ♠   ♠6|
----------
""",
"""
----------
|7 ♠   ♠ |
|    ♠   |
|  ♠   ♠ |
|        |
|  ♠   ♠7|
----------
""",
"""
----------
|8 ♠   ♠ |
|    ♠   |
|  ♠   ♠ |
|    ♠   |
|  ♠   ♠8|
----------
""",
"""
----------
|9 ♠   ♠ |
|  ♠   ♠ |
|    ♠   |
|  ♠   ♠ |
|  ♠   ♠9|
----------
""",
"""
---------- 
|10 ♠   ♠|
|  ♠ ♠ ♠ |
|        |	
| ♠ ♠ ♠  |
| ♠   ♠10|
----------
""",
"""
----------
|J   ♠   |
|    ♠   |
|    ♠   |
|    ♠   |
|    ♠  J|
----------
""",
"""
----------
|Q   ♠   |
|    ♠   |
|    ♠   |
|    ♠   |
|    ♠  Q|
----------
""",
"""
----------
|K   ♠   |
|    ♠   |
|    ♠   |
|    ♠   |
|    ♠  K|
----------
""",
"""
----------
|A       |
|        |
|    ♦   |
|        |
|       A|
----------
""",
"""
----------
|2   ♦   |
|        |
|        |
|        |
|    ♦  2|
----------
""",
"""
----------
|3   ♦   |
|        |
|    ♦   |
|        |
|    ♦  3|
----------
""",
"""
----------
|4 ♦   ♦ |
|        |
|        |
|        |
|  ♦   ♦4|
----------
""",
"""
----------
|5 ♦   ♦ |
|        |
|    ♦   |
|        |
|  ♦   ♦5|
----------
""",
"""
----------
|6 ♦   ♦ |
|        |
|  ♦   ♦ |
|        |
|  ♦   ♦6|
----------
""",
"""
----------
|7 ♦   ♦ |
|    ♦   |
|  ♦   ♦ |
|        |
|  ♦   ♦7|
----------
""",
"""
----------
|8 ♦   ♦ |
|    ♦   |
|  ♦   ♦ |
|    ♦   |
|  ♦   ♦8|
----------
""",
"""
----------
|9 ♦   ♦ |
|  ♦   ♦ |
|    ♦   |
|  ♦   ♦ |
|  ♦   ♦9|
----------
""",
"""
----------
|10 ♦   ♦|
|  ♦ ♦ ♦ |
|        |
| ♦ ♦ ♦  |
| ♦   ♦10|
----------
""",
"""
----------
|J   ♦   |
|    ♦   |
|    ♦   |
|    ♦   |
|    ♦  J|
----------
""",
"""
----------
|Q   ♦   |
|    ♦   |
|    ♦   |
|    ♦   |
|    ♦  Q|
----------
""",
"""
----------
|K   ♦   |
|    ♦   |
|    ♦   |
|    ♦   |
|    ♦  K|
----------
""",
"""
----------
|A       |
|        |
|    ♥   |
|        |
|       A|
----------
""",
"""
----------
|2   ♥   |
|        |
|        |
|        |
|    ♥  2|
----------
""",
"""
----------
|3   ♥   |
|        |
|    ♥   |
|        |
|    ♥  3|
----------
""",
"""
----------
|4 ♥   ♥ |
|        |
|        |
|        |
|  ♥   ♥4|
----------
""",
"""
----------
|5 ♥   ♥ |
|        |
|    ♥   |
|        |
|  ♥   ♥5|
----------
""",
"""
----------
|6 ♥   ♥ |
|        |
|  ♥   ♥ |
|        |
|  ♥   ♥6|
----------
""",
"""
----------
|7 ♥   ♥ |
|    ♥   |
|  ♥   ♥ |
|        |
|  ♥   ♥7|
----------
""",
"""
----------
|8 ♥   ♥ |
|    ♥   |
|  ♥   ♥ |
|    ♥   |
|  ♥   ♥8|
----------
""",
"""
----------
|9 ♥   ♥ |
|  ♥   ♥ |
|    ♥   |
|  ♥   ♥ |
|  ♥   ♥9|
----------
""",
"""
----------
|10 ♥   ♥|
|  ♥ ♥ ♥ |
|        |
| ♥ ♥ ♥  |
| ♥   ♥10|
----------
""",
"""
----------
|J   ♥   |
|    ♥   |
|    ♥   |
|    ♥   |
|    ♥  J|
----------
""",
"""
----------
|Q   ♥   |
|    ♥   |
|    ♥   |
|    ♥   |
|    ♥  Q|
----------
""",
"""
----------
|K   ♥   |
|    ♥   |
|    ♥   |
|    ♥   |
|    ♥  K|
----------
""",
"""
----------
|A       |
|        |
|    ♣   |
|        |
|       A|
----------
""",
"""
----------
|2   ♣   |
|        |
|        |
|        |
|    ♣  2|
----------
""",
"""
----------
|3   ♣   |
|        |
|    ♣   |
|        |
|    ♣  3|
----------
""",
"""
----------
|4 ♣   ♣ |
|        |
|        |
|        |
|  ♣   ♣4|
----------
""",
"""
----------
|5 ♣   ♣ |
|        |
|    ♣   |
|        |
|  ♣   ♣5|
----------
""",
"""
----------
|6 ♣   ♣ |
|        |
|  ♣   ♣ |
|        |
|  ♣   ♣6|
----------
""",
"""
----------
|7 ♣   ♣ |
|    ♣   |
|  ♣   ♣ |
|        |
|  ♣   ♣7|
----------
""",
"""
----------
|8 ♣   ♣ |
|    ♣   |
|  ♣   ♣ |
|    ♣   |
|  ♣   ♣8|
----------
""",
"""
----------
|9 ♣   ♣ |
|  ♣   ♣ |
|    ♣   |
|  ♣   ♣ |
|  ♣   ♣9|
----------
""",
"""
----------
|10 ♣   ♣|
|  ♣ ♣ ♣ |
|        |
| ♣ ♣ ♣  |
| ♣   ♣10|
----------
""",
"""
----------
|J   ♣   |
|    ♣   |
|    ♣   |
|    ♣   |
|    ♣  J|
----------
""",
"""
----------
|Q   ♣   |
|    ♣   |
|    ♣   |
|    ♣   |
|    ♣  Q|
----------
""",
"""
----------
|K   ♣   |
|    ♣   |
|    ♣   |
|    ♣   |
|    ♣  K|
----------
"""
]
def printCard(rankname = None, suitname = None):
	ranks = [
	         "ace", "two", "three", "four",
	         "five", "six", "seven", "eight",
	         "nine", "ten", "jack", "queen", "king"]
	suits = ['spades', 'diamonds', 'hearts', 'clubs']
	if suitname.lower() in suits and rankname.lower() in ranks:
		print cardStrs[suits.index(suitname.lower())*13 + ranks.index(rankname.lower())]
	else:
		print '404: card not found'
