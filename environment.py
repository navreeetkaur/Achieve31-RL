import numpy as np 
import pandas as pd

class Card():
	def __init__(self, color, value):
		self.color = color
		self.value = value

	def print(self):
		print(self.color+" "+str(self.value))

class Deck():
	def __init__(self, black_prob=2/3, red_prob=1/3, min_val=1, max_val=10):
		self.black_prob = black_prob
		self.red_prob = red_prob
		self.min_val = min_val
		self.max_val = max_val

	def sample(self):
		card_colors = ['black', 'red']
		color = np.random.choice(card_colors, p=[self.black_prob, self.red_prob])
		value = np.random.randint(self.min_val, self.max_val+1)
		return Card(color, value)
		

class State():
	def __init__(self, agent_score, dealer_score, terminated):
		self.agent_score = agent_score
		self.dealer_score  = dealer_score
		self.terminated = terminated

	def print(self):
		print("((",self.agent_score, self.dealer_score, self.terminated, "))")

		
class Human():
	def __init__(self, deck):
		self.cards = [deck.sample()]
		if self.cards[0].color=='red':
			self.busted = True
			self.score = -1*self.cards[0].value
		else:
			self.busted = False
			self.score = self.cards[0].value

	# return True if human can continue to hit, else return false
	def hit(self, deck):
		card = deck.sample()
		self.cards.append(card)
		value = -1*card.value if card.color=='red' else card.value
		self.score += value
		if self.score<0 or self.score>31:
			self.busted = True

	def print_cards(self):
		for card in self.cards:
			card.print()
		

class GameInstance():
	def __init__(self):
		self.deck = Deck()
		self.agent = Human(self.deck)
		self.dealer = Human(self.deck)

	def initial_state(self):
		if self.agent.busted and self.dealer.busted:
			reward = 0
		elif self.agent.busted:
			reward = -1
		elif self.dealer.busted:
			reward =  1
		else:
			reward =  0
		if self.agent.busted or self.dealer.busted:
			terminal = True
		else:
			terminal = False
		return [State(self.agent.score, self.dealer.score, terminal), reward, terminal]

	def reward(self):
		if self.agent.busted and self.dealer.busted:
			return 0
		elif self.agent.busted:
			return -1
		elif self.dealer.busted:
			return 1
		elif self.agent.score > self.dealer.score:
			return 1
		elif self.agent.score < self.dealer.score:
			return -1
		else:
			return 0

	def dealer_hits(self,hit):
		while self.dealer.score<25:
			self.dealer.hit(self.deck)
		else:
			self.dealer.stick()

	def step(self, hit):
		if hit:
			self.agent.hit(self.deck)
			if self.agent.busted:
				end_episode = True
				reward = -1
			else:
				end_episode = False
				reward = 0
			return [State(self.agent.score, self.dealer.score, end_episode), reward, end_episode]
		else:
			while self.dealer.score<25:
				self.dealer.hit(self.deck)
				if self.dealer.busted:
					reward = 1
					return [State(self.agent.score, self.dealer.score, True), reward, True]
			if self.dealer.score > self.agent.score:
				return [State(self.agent.score, self.dealer.score, True), -1, True]
			elif self.agent.score > self.dealer.score:
				return [State(self.agent.score, self.dealer.score, True), 1, True]
			else:
				return [State(self.agent.score, self.dealer.score, True), 0, True]









		