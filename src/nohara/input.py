import pygame
from . import data
from . import bgtext

# ============================================================
# Input Handling
# ============================================================


def handle_keydown(ev):
    mods = pygame.key.get_mods()

    # --- Camera pan (Shift + arrows) ---
    if mods & pygame.KMOD_SHIFT:
        if ev.key == pygame.K_LEFT:
            data.CAM["x"] -= 1
        elif ev.key == pygame.K_RIGHT:
            data.CAM["x"] += 1
        elif ev.key == pygame.K_UP:
            data.CAM["y"] -= 1
        elif ev.key == pygame.K_DOWN:
            data.CAM["y"] += 1
        return

    # --- Caret movement ---
    step = 2 if (mods & pygame.KMOD_CTRL) else 1

    if ev.key == pygame.K_LEFT:
        data.CARET["x"] -= step
    elif ev.key == pygame.K_RIGHT:
        data.CARET["x"] += step
    elif ev.key == pygame.K_UP:
        data.CARET["y"] -= step
    elif ev.key == pygame.K_DOWN:
        data.CARET["y"] += step

    # --- Backspace ---
    elif ev.key == pygame.K_BACKSPACE:
        bgtext.backspace()

    # --- Enter ---
    elif ev.key == pygame.K_RETURN:
        data.CARET["y"] += 1

    # --- Printable characters ---
    elif ev.unicode and ev.unicode.isprintable():
        bgtext.insert_char(ev.unicode)
