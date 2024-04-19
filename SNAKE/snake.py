import pygame

SEGMENT_SIZE = 20
GREEN = (0, 255, 0)
OBWODKA = (255, 255, 255)

class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawx(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x, self.y, SEGMENT_SIZE, SEGMENT_SIZE)) 
        pygame.draw.rect(surface, OBWODKA, (self.x, self.y, SEGMENT_SIZE, SEGMENT_SIZE), 1)

class Snake:
    def __init__(self, food, WIDTH, HEIGHT):
        self.segments = [Segment(WIDTH / 2, HEIGHT / 2)]
        self.direction = 'RIGHT'
        self.length = 1
        self.food = food
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def move(self):
        head = self.segments[0]
        x, y = head.x, head.y

        if self.direction == 'UP':
            y -= SEGMENT_SIZE
        elif self.direction == 'DOWN':
            y += SEGMENT_SIZE
        elif self.direction == 'LEFT':
            x -= SEGMENT_SIZE
        elif self.direction == 'RIGHT':
            x += SEGMENT_SIZE
            
        new_segment = Segment(x, y)
        self.segments.insert(0, new_segment)

        if x < 0 or x >= self.WIDTH or y < 0 or y >= self.HEIGHT:
            return True
        
        for segment in self.segments[1:]:
            if x == segment.x and y == segment.y:
                return True



        if self.segments[0].x == self.food.x and self.segments[0].y == self.food.y:
            self.length += 1
            self.food.generate_new_location(self.WIDTH, self.HEIGHT)

        if len(self.segments) > self.length:
            self.segments.pop()

        return False

    def draw(self, surface):
        for segment in self.segments:
            segment.drawx(surface)
