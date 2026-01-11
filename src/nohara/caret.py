import pygame
from . import data
from . import world

# ============================================================
# Caret
# ============================================================

CARET_COLOR = (255, 200, 80)
NODE_CARET_COLOR = (100, 180, 255)


def draw_caret(screen):
    # --- Cell caret ---
    sx, sy = world.cell_to_screen(data.CARET["x"], data.CARET["y"])
    rect = pygame.Rect(sx, sy, data.CELL_W, data.CELL_H)
    pygame.draw.rect(screen, CARET_COLOR, rect, 2)

    # --- Node caret (2-cell wide) ---
    node_x = (data.CARET["x"] // 2) * 2
    node_y = data.CARET["y"]

    nsx, nsy = world.cell_to_screen(node_x, node_y)
    nrect = pygame.Rect(nsx, nsy, data.CELL_W * 2, data.CELL_H)
    pygame.draw.rect(screen, NODE_CARET_COLOR, nrect, 1)


