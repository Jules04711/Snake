# Python Snake Game

A classic Snake game implementation using Pygame. The player controls a snake that grows longer as it eats food while avoiding walls and itself. This version includes multiple lives and a trophy system based on your score achievements.

## Video


https://github.com/user-attachments/assets/deb04664-7923-4836-8c00-da06edbc13c2


## Features

- Smooth snake movement with arrow key controls
- Score tracking system with high score display
- Lives system (3 lives per game)
- Trophy system with Bronze, Silver, and Gold awards
- Game over screen with play again option
- Collision detection for walls and self-collision
- Clean, minimalist visual design

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Ensure you have Python installed on your system
2. Install Pygame using pip:
    ```bash
    pip install pygame
    ```
3. Download the game files
4. Run the game:
    ```bash
    python snake_game.py
    ```

## How to Play

- Use the arrow keys to control the snake's direction:
    - ↑ (Up Arrow): Move up
    - ↓ (Down Arrow): Move down
    - ← (Left Arrow): Move left
    - → (Right Arrow): Move right
- Eat the red food blocks to grow and increase your score
- Avoid hitting the walls or running into yourself
- You have 3 lives before game over
- Try to achieve the highest score possible to earn better trophies

## Trophy System

- Bronze Trophy: Score < 10 points
- Silver Trophy: Score 10-39 points
- Gold Trophy: Score 40+ points

## Game Controls

- Arrow Keys: Control snake direction
- Space: Restart game (after game over)
- Q: Quit game (after game over)

## Technical Details

- Window Size: 800x600 pixels
- Grid Size: 20x20 pixels
- Frame Rate: 10 FPS
- Colors:
    - Snake: Green
    - Food: Red
    - Background: Black
    - Score Display: White
    - Lives Display: Yellow

## Contributing

Feel free to fork this project and submit pull requests with improvements. Some potential areas for enhancement:
- Add sound effects
- Implement different difficulty levels
- Add power-ups
- Create a high score leaderboard
- Add different game modes
