import pygame
from . import data

# ============================================================
# World / Camera / Grid
# ============================================================

GRID_COLOR = (50, 50, 50)
NODE_GRID_COLOR = (80, 80, 80)
BG_COLOR = (10, 10, 10)


def cell_to_screen(cx, cy):
    sx = (cx - data.CAM["x"]) * data.CELL_W + data.SCREEN_W // 2
    sy = (cy - data.CAM["y"]) * data.CELL_H + data.SCREEN_H // 2
    return sx, sy


def screen_to_cell(sx, sy):
    cx = (sx - data.SCREEN_W // 2) // data.CELL_W + data.CAM["x"]
    cy = (sy - data.SCREEN_H // 2) // data.CELL_H + data.CAM["y"]
    return cx, cy


def draw_grid(screen):
    cols = data.SCREEN_W // data.CELL_W + 4
    rows = data.SCREEN_H // data.CELL_H + 4

    start_x = data.CAM["x"] - cols // 2
    start_y = data.CAM["y"] - rows // 2

    # Vertical lines (cell + node)
    for i in range(cols):
        cx = start_x + i
        sx, _ = cell_to_screen(cx, data.CAM["y"])

        if cx % 2 == 0:
            color = NODE_GRID_COLOR
            width = 2
        else:
            color = GRID_COLOR
            width = 1

        pygame.draw.line(screen, color, (sx, 0), (sx, data.SCREEN_H), width)

    # Horizontal lines (cells only for now)
    for j in range(rows):
        cy = start_y + j
        _, sy = cell_to_screen(data.CAM["x"], cy)
        pygame.draw.line(screen, GRID_COLOR, (0, sy), (data.SCREEN_W, sy), 1)
