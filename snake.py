import pygame
import random
import time
#from pygame import mixer 

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)  # For lives display

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Add after other constants
BRONZE_TROPHY = "BRONZE"
SILVER_TROPHY = "SILVER"
GOLD_TROPHY = "GOLD"

class Snake:
    def __init__(self):
        self.reset()

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)
        
        # Check for wall collision - game over immediately
        if (new[0] < 0 or new[0] >= GRID_WIDTH or 
            new[1] < 0 or new[1] >= GRID_HEIGHT):
            return "wall"
        
        # Check for self collision - lose a life
        if new in self.positions[2:]:
            return "self"
        
        # If no collisions, update position
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return "ok"

    def reset(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, GREEN,
                           (p[0] * GRID_SIZE, p[1] * GRID_SIZE,
                            GRID_SIZE - 2, GRID_SIZE - 2))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1),
                        random.randint(0, GRID_HEIGHT - 1))

    def render(self, surface):
        pygame.draw.rect(surface, RED,
                        (self.position[0] * GRID_SIZE,
                         self.position[1] * GRID_SIZE,
                         GRID_SIZE - 2, GRID_SIZE - 2))

def show_game_over_screen(screen, final_score):
    # Update trophy criteria and display
    if final_score < 10:
        trophy = BRONZE_TROPHY
        trophy_color = (205, 127, 50)  # Bronze color
        trophy_text = "Bronze Trophy"
    elif final_score < 40:
        trophy = SILVER_TROPHY
        trophy_color = (192, 192, 192)  # Silver color
        trophy_text = "Silver Trophy"
    else:
        trophy = GOLD_TROPHY
        trophy_color = (255, 215, 0)    # Gold color
        trophy_text = "Gold Trophy"
    
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.fill(BLACK)
    overlay.set_alpha(230)
    screen.blit(overlay, (0,0))
    
    # Modified font sizes for better visibility
    trophy_font = pygame.font.Font(None, 96)  # Slightly smaller than before
    regular_font = pygame.font.Font(None, 64)
    
    # Render all text elements
    game_over_text = regular_font.render('GAME OVER', True, RED)
    score_text = regular_font.render(f'Final Score: {final_score}', True, WHITE)
    trophy_text = trophy_font.render(trophy, True, trophy_color)
    play_again_text = regular_font.render('Press SPACE to Play Again', True, GREEN)
    quit_text = regular_font.render('Press Q to Quit', True, RED)
    
    # Position all elements with more spacing
    screen.blit(game_over_text, 
                (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                 WINDOW_HEIGHT//2 - 180))
    screen.blit(score_text, 
                (WINDOW_WIDTH//2 - score_text.get_width()//2, 
                 WINDOW_HEIGHT//2 - 100))
    screen.blit(trophy_text, 
                (WINDOW_WIDTH//2 - trophy_text.get_width()//2, 
                 WINDOW_HEIGHT//2))
    screen.blit(play_again_text, 
                (WINDOW_WIDTH//2 - play_again_text.get_width()//2, 
                 WINDOW_HEIGHT//2 + 120))
    screen.blit(quit_text, 
                (WINDOW_WIDTH//2 - quit_text.get_width()//2, 
                 WINDOW_HEIGHT//2 + 180))
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
    return False

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    lives = 3
    high_score = 71

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        # Update snake position
        result = snake.update()
        
        if result == "wall" or result == "self":
            lives -= 1
            if lives <= 0:
                # Show game over screen and handle restart
                if show_game_over_screen(screen, score):
                    # Reset everything for a new game
                    snake.reset()
                    food.randomize_position()
                    score = 0
                    lives = 3
                else:
                    return  # Quit the game
            else:
                # Reset snake position but keep score
                snake.reset()
                food.randomize_position()
            time.sleep(1)
            continue

        # Check if snake ate food
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()

        # Draw everything
        screen.fill(BLACK)
        snake.render(screen)
        food.render(screen)
        
        # Display score and lives
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        high_score_text = font.render(f'High Score: {high_score}', True, WHITE)
        lives_text = font.render(f'Lives: {lives}', True, YELLOW)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WINDOW_WIDTH - 120, 10))
        screen.blit(high_score_text, (WINDOW_WIDTH // 2 - high_score_text.get_width() // 2, 10))
        
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
