import pygame
from abc import ABC, abstractmethod

#position needs to be y, x
class Tile(ABC):
	def __init__(self, position = None):
		self.position = position
	
	def display(self, screen):
		y, x = self.position
		if (y + x) % 2 == 0:
			y = (y * 100) + 50
			x = (x * 100) + 50

			self.tile = pygame.image.load("img/dark_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (50, 50))
			self.tile_rect = self.tile.get_rect(center = (y, x))
			screen.blit(self.tile, (x, y))
		
		if (y + x) % 2 == 1:
			y = (y * 100) + 50
			x = (x * 100) + 50

			self.tile = pygame.image.load("img/light_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (50, 50))
			self.tile_rect = self.tile.get_rect(center = (y, x))
			screen.blit(self.tile, (x, y))

class Bomb(Tile):
	def __init__(self, position):
		super().__init__(position)
		#Make this part of the parent class if possible
		self.y, self.x = position
	
	def __str__(self):
		return "x"

	def display(self):
		# screen.blit(thingies)
		pass


		

class Blank(Tile):
	def __init__(self, position = None):
		super().__init__(position)
		y, x = position
	
	def __str__(self):
		return "Blank"
	


class Cover(Tile):
	def __init__(self, position = None):
		super().__init__(position)
		y, x = position
		# screen.blit(thingies)


	def __str__(self):
		return "Cover"
	
	def clicked(self):
		del self

class Number(Tile):
	def __init__(self, position = None, number = 0):
		super().__init__(position)
		y, x = position
		self.number = number

	def __str__(self):
		return str(self.number)

	def display(self):
		# screen.blit(thingies)
		pass