import pygame
from abc import ABC, abstractmethod

#position needs to be y, x
class Tile(ABC):
	def __init__(self, position = None):
		self.position = position
		self.font = pygame.font.SysFont(None, 48)
	
	def display(self, screen):
		# print("this is display from Tile", type(self))
		y, x = self.position
		if (y + x) % 2 == 0:
			y = (y * 100)
			x = (x * 100)

			self.tile = pygame.image.load("img/dark_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (100, 100))
			self.tile_rect = self.tile.get_rect(center = (y, x))
			screen.blit(self.tile, (x, y))
		
		if (y + x) % 2 == 1:
			y = (y * 100)
			x = (x * 100)

			self.tile = pygame.image.load("img/light_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (100, 100))
			self.tile_rect = self.tile.get_rect(center = (y, x))
			screen.blit(self.tile, (x, y))

class Bomb(Tile):
	def __init__(self, position):
		super().__init__(position)
		#Make this part of the parent class if possible
		self.y, self.x = position
	
	def __str__(self):
		return "x"
	
	def display(self, screen):
		super().display(screen)
		self.bomb = pygame.image.load("img/bomb_img.png")
		screen.blit(self.bomb, self.tile_rect)

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
	
	def display(screen):
		# super.display(screen)
		pass
	
	def clicked(self):
		del self

class Number(Tile):
	def __init__(self, position = None, number = 0):
		super().__init__(position)
		self.y, self.x = position
		self.number = number

	def __str__(self):
		return str(self.number)
	
	def display(self, screen):
		super().display(screen)
		surface = self.font.render(str(self.number), True, (225, 0, 0))
		print(self.tile_rect)
		screen.blit(surface, self.tile_rect)