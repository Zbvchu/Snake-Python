import pygame
from snake import Snake
from jedzenie import Food

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Nokia 3310")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def game_over():
    font = pygame.font.SysFont(None, 50)
    font2 = pygame.font.SysFont(None, 35)
    text = font.render("PRZEGRAŁEŚ", True, (255, 255, 255))
    text2 = font2.render("KLIKNIJ ENTER ABY ZACZAC OD NOWA", True, (255, 255, 255))
    text_rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 1.8))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(text, text_rect)
    WIN.blit(text2, text_rect2)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False  
                    main()
    
def main():
    clock = pygame.time.Clock()
    food = Food(WIDTH, HEIGHT)
    snake = Snake(food, WIDTH, HEIGHT)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_w and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_a and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_d and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_s and snake.direction != 'UP':
                    snake.direction = 'DOWN'

        if snake.move():
            game_over()

        WIN.fill(BLACK)
        snake.draw(WIN)
        food.draw(WIN)
        font3 = pygame.font.SysFont(None, 35)
        text3 = font3.render("WYNIK: " + str(len(snake.segments)-1), True, WHITE)
        text_rect3 = text3.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
        WIN.blit(text3, text_rect3)
        pygame.display.update()
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()
