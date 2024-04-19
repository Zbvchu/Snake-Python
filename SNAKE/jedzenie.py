import pygame
import random

SEGMENT_SIZE = 20
RED = (255, 0, 0)

class Food:
    def __init__(self, WIDTH, HEIGHT):
        self.generate_new_location(WIDTH, HEIGHT)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, SEGMENT_SIZE, SEGMENT_SIZE))
    
    def generate_new_location(self, WIDTH, HEIGHT):
        self.x = random.randint(0, (WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
        self.y = random.randint(0, (HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
