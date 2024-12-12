import pygame
from abc import ABC, abstractmethod

#position needs to be y, x
class Tile(ABC):
	def __init__(self, position = None):
		self.position = position
		self.font = pygame.font.SysFont(None, 48)
		self.y, self.x = self.position
	
	def display(self, screen):
		converted_y = (self.y * 100) 
		converted_x = (self.x * 100)
		if (self.y + self.x) % 2 == 0:
			self.tile = pygame.image.load("img/dark_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (100, 100))
			self.tile_rect = self.tile.get_rect(center = (converted_x, converted_y))
			screen.blit(self.tile, (converted_x, converted_y))
		
		if (self.y + self.x) % 2 == 1:
			self.tile = pygame.image.load("img/light_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (100, 100))
			self.tile_rect = self.tile.get_rect(center = (converted_x, converted_y))
			screen.blit(self.tile, (converted_x, converted_y))
		

class Bomb(Tile):
	def __init__(self, position):
		super().__init__(position)
		self.font = pygame.font.SysFont(None, 24)
	
	def __str__(self):
		return "x"
	
	def display(self, screen):
		super().display(screen)
		self.bomb = pygame.image.load("img/bomb_img.png")
		self.bomb = pygame.transform.scale(self.bomb, (75, 75))
		self.tile_rect.centerx += 75
		self.tile_rect.centery += 50
		screen.blit(self.bomb, self.tile_rect)

		surface = self.font.render(f"{self.x}, {self.y}", True, (225, (self.y + self.x) * 10, 0))

		screen.blit(surface, self.tile_rect)

		#print("This is Bomb's display method: ", self.x, self.y)


class Blank(Tile):
	def __init__(self, position = None):
		super().__init__(position)
	
	def __str__(self):
		return "Blank"
	

class Cover(Tile):
	def __init__(self, position = None):
		super().__init__(position)
		# screen.blit(thingies)


	def __str__(self):
		return "cover"
	
	def display(self, screen):
		print("Called")
		super().display(screen)
	
	def clicked(self):
		del self

class Number(Tile):
	def __init__(self, position = None, number = 0):
		super().__init__(position)
		self.number = number

	def __str__(self):
		return str(self.number)
	
	def display(self, screen):
		super().display(screen)

		#surface = self.font.render(f"{self.number}, x: {self.x}, y{self.y}", True, (225, (self.y + self.x) * 10, 0))
		surface = self.font.render(f"{self.number}", True, (225, (self.y + self.x) * 10, 0))

		#print("This is Number's display method: ", self.y, self.x)

		self.tile_rect.centerx += 75 + 12
		self.tile_rect.centery += 75 + 12

		screen.blit(surface, self.tile_rect)
