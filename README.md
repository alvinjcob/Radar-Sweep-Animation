# Radar Sweep Animation

A simple radar sweep animation with simulated targets, implemented in Python using the `pygame` library.
This project uses a custom implementation of the **Bresenham Line Algorithm** to draw the sweeping radar arm.

## Features

- **Radar UI:** Renders a classic dark green radar interface with distance rings and crosshairs.
- **Bresenham Algorithm:** Instead of standard line drawing, the radar sweep is drawn pixel-by-pixel using a software implementation of the Bresenham line algorithm.
- **Target Simulation:** Randomly places targets across the circular range.
- **Sweep Detection:** As the radar line sweeps across the angle of a target, the target briefly lights up in bright green to simulate radar detection.

## Prerequisites

- Python 3.x
- [Pygame](https://www.pygame.org/)

## Installation

1. Ensure Python 3 is installed.
2. Install the `pygame` and necessary dependencies:
   ```bash
   pip install pygame
   ```

## Usage

Run the `radar.py` script directly from your terminal:

```bash
python radar.py
```

Close the Pygame window to stop the animation.
