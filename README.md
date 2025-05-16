# Alien Invasion (Python Game)

**Alien Invasion** is a 2D shooting game developed using [Pygame](https://www.pygame.org/) as part of the *Python Crash Course* book project. This README describes the current state of the game and the structure of the codebase.

---

## 🚀 Current Features

- Initializes a window with a ship displayed at the bottom center.
- Ship can move left and right using arrow keys.
- The game screen updates smoothly in a loop.
- Modular code split across files for clarity and scalability.

---

## 📁 Project Structure

```
alien_invasion/
│
├── alien_invasion.py   # Main game loop and overall game logic
├── settings.py         # Game settings (screen size, ship speed, etc.)
├── ship.py             # Ship class: handles image loading, movement, drawing
└── images/
    └── ship.bmp        # Ship sprite image
```

---

## 🧠 Code Overview

### `alien_invasion.py`
- Contains the `AlienInvasion` class:
  - Initializes screen, settings, and the ship.
  - Handles the game loop using:
    - `_check_events()` – captures key events.
    - `ship.update()` – updates ship position.
    - `_update_screen()` – redraws screen each frame.

### `settings.py`
- Defines the `Settings` class:
  - Stores game configuration like screen dimensions and ship speed.

### `ship.py`
- Defines the `Ship` class:
  - Loads and scales the ship image.
  - Manages ship movement via `update()`.
  - Draws the ship using `blitme()`.

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

- Add bullet firing functionality.
- Introduce alien fleet and collision detection.
- Scorekeeping and game levels.

---

## 📚 Based on

Project from *Python Crash Course* by Eric Matthes.
