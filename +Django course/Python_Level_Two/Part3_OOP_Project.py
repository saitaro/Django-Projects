# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
from itertools import chain
endalert = True

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck(list):
	"""
	This is the Deck Class. This object will create a deck of cards to initiate
	play. You can then use this Deck list of cards to split in half and give to
	the players. It will use SUITE and RANKS to create the deck. It should also
	have a method for splitting/cutting the deck in half and Shuffling the deck.
	"""
	shuffled = False

	def __init__(self):
		self.deck = []
		for s in suite:
			for r in ranks:
				self.deck.append((s+r))

	def cut(self):
		shuffle(self.deck)
		self.shuffled = True
		self.deck = (self.deck[:26], self.deck[26:])

	def __str__(self):
		return str(self.deck)

	def __len__(self):
		if self.shuffled:
			return len(self.deck[0]) + len(self.deck[1])
		else:
			return len(self.deck)

	def __getitem__(self, index):
		return self.deck[index]

	def set(self):
		if self.shuffled:
			return set(self.deck[0]) + set(self.deck[1])
		else:
			return set(self.deck)

class Hand:
	'''
	This is the Hand class. Each player has a Hand, and can add or remove
	cards from that hand. There should be an add and remove card method here.
	'''
	def __init__(self, pool):
		self.pool = pool

	def add(self, new):
		self.pool.extend(new)
	
	def get(self, n=1, war=False, pl=None):
		if war and len(self.pool) < n:
			print('{} has not enough cards to wage the war!'.format(pl))
			print('{} won!'.format(player.name if pl == 'Computer' else 'Computer'))
			global endalert
			endalert = False
			GameOn(war)
		tool = self.pool[:n]
		del self.pool[:n]
		return str(tool[0]) if n == 1 else tool

	@property
	def state(self):
		return False if not self.pool else True

	def __str__(self):
		return str(self.pool)

	def __len__(self):
		return len(self.pool)

	@property
	def Set(self):
		return set(self.pool)

class Player:
	"""
	This is the Player class, which takes in a name and an instance of a Hand
	class object. The Player can then play cards and check if they still have cards.
	"""
	def __init__(self, name):
		self.name = name

print("Welcome to War, let's begin...")

player = Player(input("Enter you name: "))

main = Deck()
main.cut()

playerHand = Hand(main[0])
compHand = Hand(main[1])

def stat():
	print('Comp:\n', compHand, len(compHand), 'cards total', '\nYou:\n', playerHand, len(playerHand), 'cards total', '\n')

print("Everything is ready now, let's begin the War!\n")

def GameOn(war=False):
	global endalert
	if ((playerHand.state and compHand.state) or war) and endalert:
		return True
	if endalert:
		print('Game over')
		if not playerHand.state:
			print('Computer won!')
		else:
			print('{} won!'.format(player.name))
		endalert = False
	return False

def rank(game, war=False):
	if war:
		return ranks.index(game[0][-1][1:]), ranks.index(game[1][-1][1:])
	return ranks.index(game[0][1:]), ranks.index(game[1][1:])

while GameOn():

	game = [playerHand.get(), compHand.get()]
	rankPlayer, rankComp = rank(game)

	print('The game is {}'.format(game))
	print("Your card {} (rank {}) vs {} (rank {}) Computer's card".format(game[0], rankPlayer, game[1], rankComp))

	if rankPlayer > rankComp:

		print('You won this round and get {} and {} into your deck'.format(game[0], game[1]))
		playerHand.add(game[::-1])
		stat()
		if not GameOn():
			break

	elif rankPlayer < rankComp:

		print('The computer won this round and gets {} and {} into his deck'.format(game[0], game[1]))
		compHand.add(game)
		stat()
		if not GameOn():
			break

	else:
		war = True

		print("=***= The cards are of equal power, it is War! =***=")
		game[0] = [game[0]] + playerHand.get(2, war, player.name)
		game[1] = [game[1]] + compHand.get(2, war, 'Computer')
		if not GameOn(war):
			break

		while war and endalert:
			print('game is {}'.format(game))
			rankPlayer, rankComp = rank(game, war)
			print('Cards: Player {} (rank {}) vs {} (rank {}) Comp'.format(game[0][-1], rankPlayer, game[1][-1], rankComp))
			if rankPlayer == rankComp:
				print('******************* War goes on! *******************')
				game[0].extend(playerHand.get(2, war=True, pl=player.name))
				game[1].extend(compHand.get(2, war=True, pl='Computer'))
				# if not GameOn():
				# 	break
			else:
				war = False
				if rankPlayer > rankComp:
					print('{} won this round and gets {} into his deck'.format(player.name, list(chain.from_iterable(game))))
					playerHand.add(game[1]+game[0])
					stat()
				else:
					print('The computer won this round and gets {} into his deck'.format(list(chain.from_iterable(game))))
					compHand.add(game[0]+game[1])
					stat()
