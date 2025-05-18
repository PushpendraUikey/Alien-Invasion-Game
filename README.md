# Alien Invasion (Python Game)

**Alien Invasion** is a 2D shooting game developed using [Pygame](https://www.pygame.org/) as part of the *Python Crash Course* book project. This README describes the current state of the game and the structure of the codebase.

---

## 🚀 Current Features

- Initializes a window with a ship displayed at the bottom center.
- Ship can move left and right using arrow keys.
- Ship can fire bullets upward using the spacebar.
- Bullets move up the screen and are removed when off-screen.
- The game screen updates smoothly in a loop.
- Modular code split across files for clarity and scalability.

---

## 📁 Project Structure

```
alien_invasion/
│
├── alien_invasion.py   # Main game loop and overall game logic
├── settings.py         # Game settings (screen size, speeds, colors)
├── ship.py             # Ship class: handles image loading, movement, drawing
├── bullet.py           # Bullet class: manages firing, movement, rendering
└── images/
    └── ship.bmp        # Ship sprite image
```

---

## 🧠 Code Overview

### `alien_invasion.py`
- Contains the `AlienInvasion` class:
  - Initializes screen, settings, ship, and bullet group.
  - Handles the game loop using:
    - `_check_events()` – captures key events (movement, firing).
    - `ship.update()` – updates ship position.
    - `bullets.update()` – updates bullet positions and removes off-screen bullets.
    - `_update_screen()` – redraws screen each frame.

### `settings.py`
- Defines the `Settings` class:
  - Stores game configuration like screen dimensions, speeds, and bullet settings.

### `ship.py`
- Defines the `Ship` class:
  - Loads and scales the ship image.
  - Manages ship movement via `update()`.
  - Draws the ship using `blitme()`.

### `bullet.py`
- Defines the `Bullet` class:
  - Creates bullet rect and sets its initial position.
  - Moves bullets upward using `update()`.
  - Renders bullets using `draw_bullet()`.

---

## ▶️ How to Run

1. Install Pygame (if not already):
   ```bash
   pip install pygame
   ```
2. Run the game:
   ```bash
   python alien_invasion.py
   ```

---

## 📌 To-Do (Next Steps)

- Introduce alien fleet and collision detection.
- Scorekeeping and game levels.

---

## 📚 Based on

Project from *Python Crash Course* by Eric Matthes.
