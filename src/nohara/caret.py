import pygame
from . import data
from . import world

# ============================================================
# Caret
# ============================================================

CARET_COLOR = (255, 200, 80)


def draw_caret(screen):
    sx, sy = world.cell_to_screen(data.CARET["x"], data.CARET["y"])
    rect = pygame.Rect(sx, sy, data.CELL_W, data.CELL_H)
    pygame.draw.rect(screen, CARET_COLOR, rect, 2)
