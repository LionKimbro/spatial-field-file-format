import pygame
from . import data
from . import world

# ============================================================
# Background Text Layer
# ============================================================

TEXT_COLOR = (230, 230, 230)

_font = None


def init_font():
    global _font
    if _font is None:
        _font = pygame.font.Font(None, 16)


def draw_bg_text(screen):
    if _font is None:
        init_font()

    for (cx, cy), ch in data.BG_TEXT.items():
        sx, sy = world.cell_to_screen(cx, cy)
        surf = _font.render(ch, True, TEXT_COLOR)
        screen.blit(surf, (sx, sy))


def insert_char(ch):
    x = data.CARET["x"]
    y = data.CARET["y"]
    data.BG_TEXT[(x, y)] = ch
    data.CARET["x"] += 1


def backspace():
    x = data.CARET["x"]
    y = data.CARET["y"]

    if (x, y) in data.BG_TEXT:
        del data.BG_TEXT[(x, y)]

    data.CARET["x"] -= 1
